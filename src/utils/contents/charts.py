__all__ = ['show_price_history_graph_popup']
from typing import Any

from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pywebio.output import PopupSize, close_popup, popup, put_html
from src.database.utils import get_product_price_history
from src.settings import LOCAL_TIMEZONE


def plot_price_history_line_graph(data: list[dict[str, Any]]) -> None:
    """
    Renders a line graph in the form of HTML
    """
    more_than_one_data = len(data) > 1

    chart = (
        Line()
        .add_xaxis([d['date'] for d in data])
        .add_yaxis(
            series_name='$SGD',
            y_axis=[d['price'] for d in data],
            # Mark Point
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_='min', name='Min'),
                    opts.MarkPointItem(type_='max', name='Max'),
                ],
            ) if more_than_one_data else None,
            # Mark Line
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_='average', name='Avg')],
            ) if more_than_one_data else None,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Price History', subtitle='$(SGD)'),
            yaxis_opts=opts.AxisOpts(min_='dataMin'),
        )
    )

    chart.width = '465px'
    chart.height = '400px'
    chart.theme = ThemeType.INFOGRAPHIC
    put_html(chart.render_notebook())


def show_price_history_graph_popup(self, product: dict[str, Any]) -> None:
    """
    Shows a popup rendering a line graph of the beer's historical price
    """
    @popup(title=product['name'], size=PopupSize.NORMAL)
    def show() -> None:
        product_prices = get_product_price_history(product['id'])
        if not product_prices:
            close_popup()
            return None

        data = [
            {
                'date': price.updated_on.astimezone(LOCAL_TIMEZONE).strftime('%d-%b-%y'),
                'price': round(price.price, 2),
            } for price in product_prices
        ]

        plot_price_history_line_graph(data)
    show()
