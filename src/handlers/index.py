__all__ = ['index']
from cProfile import label
import logging
from functools import partial
from pickle import TRUE
from turtle import position
from typing import Union
from pywebio.pin import *

from pywebio.input import *
from pywebio import config, session

from pywebio.io_ctrl import Output, OutputList
from pywebio.output import *
from pywebio.platform import seo
from pywebio.platform.page import config
from pywebio.session import run_js, set_env
import json
from src.database.models import Video
# from src.database.utils import get_product_based_on_query, get_random_beer, get_random_beer_brand, get_random_beer_style, get_random_results_not_found_gif
from src.settings import SEO_DESCRIPTION, SEO_TITLE
from src.utils.constants import GA_JS_CODE, GA_JS_FILE, POPULAR_BEER_BRANDS, POPULAR_BEER_STYLES, LABELS

# from src.utils.contents.charts import show_price_history_graph_popup
from src.utils.contents.index import FOOTER, HEADER, LANDING_PAGE_DESCRIPTION_English, LANDING_PAGE_DESCRIPTION_Chinese, LANDING_PAGE_HEADING, LANDING_PAGE_SUBHEADING, LOAD_CSS, PRODUCT_HUNT_FEATURED_BANNER
from src.utils.validators import validate_search_length

logger = logging.getLogger(__name__)


# def generate_table_header():
# #  -> list[Union[Output, OutputList, str]]:
#     return [
#         style(put_text('🛍\nPlatform'), 'text-align:center;'),
#         style(put_text('🍻\nName'), 'text-align:center;'),
#         style(put_text('✨\nStyle'), 'text-align:center;'),
#         style(put_text('💲\nPrice'), 'text-align:center;'),
#         style(put_text('🛒\nQty.'), 'text-align:center;'),
#         style(put_text('💸\nPrice/Qty.'), 'text-align:center;'),
#     ]


# def generate_table_data(vidoes: list[Video]):
# # -> list[list[Union[Output, OutputList, str]]]:
#     return [
#         [
#             # Platform
#             style(put_text(product.platform.title()), 'text-align:center'),
#             # Name
#             put_collapse(
#                 product.name, style(
#                     [
#                         put_table([
#                             ['Volume', 'ABV', 'Link', 'Price Chart'],
#                             [
#                                 f'{product.volume}ml' if product.volume else '🙊',
#                                 f'{product.abv}%' if product.abv else '🙈',
#                                 put_link(name='View', url=product.url,
#                                          new_window=True),
#                                 put_buttons(
#                                     [dict(label='Show', value={
#                                           'id': product.id, 'name': product.name}, color='primary')],
#                                     onclick=partial(show_price_history_graph_popup, {
#                                                     'id': product.id, 'name': product.name}),
#                                 ),
#                             ],
#                         ]),
#                     ], 'text-align:center;',
#                 ), open=False,
#             ),
#             # Style
#             style(put_text(product.style if product.style else '😬'),
#                   'text-align:center;'),
#             # Price
#             f'${product.last_price:.2f}',
#             # Qty.
#             style(put_text(product.quantity), 'text-align:center'),
#             # Price/Qty.
#             style(
#                 put_link(name=f'${product.price_per_quantity:.2f}',
#                          url=product.url, new_window=True),
#                 'color:red; font-weight:bold; text-align:center; text-decoration: underline;',
#             ),
#         ] for product in products
#     ]

@seo(SEO_TITLE, SEO_DESCRIPTION)
@config(theme="minty", js_file=[GA_JS_FILE], js_code=GA_JS_CODE)
def lang():

    popup('Choose your preferred language', [
        put_buttons(['English', 'Chinese'], onclick=index)
    ], closable=True)


def settinggif():
    # img = open('/assets/image/demo.gif', 'rb').read()
    # put_image(img, width='150px')

    put_image('https://www.python.org/static/img/python-logo.png')


def newusertour():
    put_warning('start a new user tour guide')


def videoprepare():
    print('option:already or generate')
    print('generate option:repost ytb,import tk to ytb,import ytb to tk')
    print('prepared')


def validateinstall():
    print('file is ok')
    print('load demo setting')
    print('upload to demo channel')


def showsetting(settingid):
    print('ssssssssssss', settingid)
    if 'ytb' in settingid:
        print('choose=')
        data = input_group("start configure your yotube upload rules", [
        input('used as  new setting file name', type=TEXT, name='channelname',
                placeholder='something like this UC09XXWLe76WeoRoRFMWdnCw', required=True, scope='newuploadsetting'),
        input('copy cookie json file path', type=TEXT, name='cookiefilepath',
                value=r'D:\autovideopublish\assets\cookies\harrypotter.json', required=True, scope='newuploadsetting'),
        input('choose profile folder', type=TEXT, name='profilefilepath',
                required=True, scope='newuploadsetting'),
        input('bg music folder', type=TEXT, name='bgmusicfolder',
                required=True, scope='newuploadsetting'),
        input('bgmusicvolumn', type=TEXT, name='bgmusicvolumn',
                required=True, scope='newuploadsetting'),
        input('dailypublishcount', type=TEXT, name='dailypublishcount',
                required=True, scope='newuploadsetting'),
        input('publishpolicy', type=TEXT, name='publishpolicy',
                required=True, scope='newuploadsetting'),
        input('prefertags', type=TEXT, name='prefertags',
                required=True, scope='newuploadsetting'),
        input('preferdessuffix', type=TEXT, name='preferdes',
                required=True, scope='newuploadsetting'),
        input('prefertitlesuffix', type=TEXT, name='prefertitle',
                required=True, scope='newuploadsetting'),
            actions(
            name="action",
            buttons=[
                    {"label": "Submit", "value": "submit", "color": "primary"},
                    {"label": "Reset", "type": "reset", "color": "warning"},
                    {"label": "Back", "type": "cancel", "color": "success"},
                ],
        ),
        ], validate=validatesetting)
    elif 'tk' in settingid:
        data = input_group("start configure your tiktok upload rules", [
        input('used as  new setting file name', type=TEXT, name='channelname', placeholder='something like this UC09XXWLe76WeoRoRFMWdnCw',required=True,scope='newuploadsetting'),
        input('copy cookie json file path', type=TEXT, name='cookiefilepath', value=r'D:\autovideopublish\assets\cookies\harrypotter.json',required=True,scope='newuploadsetting'),
        input('choose profile folder', type=TEXT, name='profilefilepath', required=True, scope='newuploadsetting'),
        input('bg music folder', type=TEXT, name='bgmusicfolder', required=True, scope='newuploadsetting'),
        input('bgmusicvolumn', type=TEXT, name='bgmusicvolumn', required=True, scope='newuploadsetting'),
        input('dailypublishcount', type=TEXT, name='dailypublishcount', required=True, scope='newuploadsetting'),
        input('publishpolicy', type=TEXT, name='publishpolicy', required=True, scope='newuploadsetting'),
        input('prefertags', type=TEXT, name='prefertags', required=True, scope='newuploadsetting'),
        input('preferdessuffix', type=TEXT, name='preferdes', required=True, scope='newuploadsetting'),
        input('prefertitlesuffix', type=TEXT, name='prefertitle', required=True, scope='newuploadsetting')
            ,
            actions(
            name="action",
            buttons=[
                    {"label": "Submit", "value": "submit", "color": "primary"},
                    {"label": "Reset", "type": "reset", "color": "warning"},
                    {"label": "Extra Button",
                        "type": "cancel", "color": "success"},
                    {"label": "Another Extra Button",
                        "value": "another", "color": "info"},
                ],
        ),

        ], validate=validatesetting)


@seo(SEO_TITLE, SEO_DESCRIPTION)
@config(theme="minty", js_file=[GA_JS_FILE], js_code=GA_JS_CODE)
def index(lang) -> None:
    """
    Renders the home page of autovideopublish
    """
    close_popup()
    # newusertour()
    session.run_js('WebIO._state.CurrentSession.on_session_close(()=>{setTimeout(()=>location.reload(), 40000})')    
    labels = LABELS[lang]
    set_env(auto_scroll_bottom=False)

    # JavaScript stuffs
    run_js(HEADER)
    run_js(FOOTER)
    put_html(LOAD_CSS)

    # Page heading
    put_html(LANDING_PAGE_HEADING)
    if lang == 'English':
        LANDING_PAGE_DESCRIPTION = LANDING_PAGE_DESCRIPTION_English
    elif lang == 'Chinese':
        LANDING_PAGE_DESCRIPTION = LANDING_PAGE_DESCRIPTION_Chinese
# 游戏新手引导 配合popup 图片 检测是否存在配置文件来判断是否第一次使用
    with use_scope('introduction'):
        # put_html(PRODUCT_HUNT_FEATURED_BANNER)
        # put_html(LANDING_PAGE_SUBHEADING)
        put_markdown(LANDING_PAGE_DESCRIPTION, lstrip=True)
        installok = False
        if validateinstall ==False:
            put_row([put_button("install", onclick=installrequriment,
                                color='primary', outline=False)
                     , put_button("setting", onclick=newuploadsetting,
                                 color='primary', outline=False)
                     , put_button("video prepare", onclick=videoprepare,
                                          color='primary', outline=False)
                    , put_button("upload", onclick=uploadtask,
                                            color='primary', outline=False)])
        put_row([put_button("setting", onclick=newuploadsetting,
                             color='primary', outline=False)
                  , put_button("video prepare", onclick=videoprepare,
                                          color='primary', outline=False)
                  , put_button("upload", onclick=uploadtask,
                            color='primary', outline=False)])


def installrequriment():
    clear('introduction')
    put_info('first install check, then initial setting, upload task at last')

    with use_scope('installrequriment'):
        put_button("check tool requirements", onclick=lambda: toast('ok'),
                   color='primary', outline=False)
        put_text('you have successfully install our tool')


def uploadworkflow():
    clear('introduction')
    put_info('first install check, then initial setting, upload task at last')

    with use_scope('uploadworkflow'):

        put_tabs([
            {'title': 'install', 'content': put_scope('installrequriment', content='')},
            {'title': 'setting', 'content': put_scope('newuploadsetting', content='')},
            {'title': 'upload', 'content': put_scope('uploadtask', content='')},
        ], position=0)
    # with use_scope('installrequriment', clear=True):
    #     installrequriment()

    # with use_scope('newuploadsetting', clear=True):
    #     newuploadsetting()
        # uploadtask()

def validatesetting(data):
    # cookie file exist
    # profile file exist
    # bg music folder is not empty
    pass


def newuploadsetting():
    # put_text('done')
    # clear('installrequriment')
    clear('introduction')

    with use_scope('newuploadsetting'):
        # defaultsettingfile = put_button("loading cookie file", required=True)
        settinggif()

        # read from db
        settingrules = ['default_ytb_template', 'default_tk_template','aww_ytb']
        settingid = select(label='choose your rules?',help_text='loading exist or start from template',options=settingrules,onchange=lambda val: showsetting(val)),
        rules ={
            "channelname": "xxxx",
            "cookiepath": "xxx/xxx/.json"
        }
        print('===', type(settingid))
        if settingid[0] ==settingrules[0]:
            showsetting(settingid[0])
        # print(data['cookiefilepath'])
        # put_code('info = ' + json.dumps(info, indent=4)),
        # if info is not None:
        #     if info['action'] == 'save_and_continue':
        #         put_text('Save and add next...')

# save setting


def uploadtask():
    clear('introduction')

    with use_scope('uploadtask'):
    # load setting
    # choose type  0 start from scratch  1 tiktok to youtube 2  youtube to tiktok

        # Loop Forever
        while True:
            # suggested_brand = get_random_beer_brand()
            # suggested_style = get_random_beer_style()
            # suggested_beer = get_random_beer()

            help_text = 'xxxxxxxxxxxx read doc above'
            search = input(
                type=TEXT,
                required=True,
                label='🤩 Start looking here:',
                placeholder='Search for a platform, beer brand, style, or name...',
                help_text=help_text,
                validate=validate_search_length,
                datalist=POPULAR_BEER_BRANDS + POPULAR_BEER_STYLES,
            )
            # with use_scope('introduction'):

               # put_markdown(LANDING_PAGE_DESCRIPTION, lstrip=True)

            # clear('result')
            # clear('introduction')
            # scroll_to(position='top')

            # Amplitude tracking
            run_js(
                f"amplitude.getInstance().logEvent('Keyword searched: \"{search}\"');")

            # NOTE: Because the underlying SQL is using `to_tsquery`, we have to wrap our search text with single quotes
            with style(put_loading(color='primary'), 'width:20rem; height:20rem; display:block; margin-left:auto; margin-right:auto;'):
                # products = get_product_based_on_query(str(search).lower())

                with use_scope('result'):
                    if not products:
                        put_html(get_random_results_not_found_gif())
                        put_html(
                            f'<h2 align="center">😢 Oh no, we couldn\'t find anything related to <i>"{search}"</i>...</h2>')
                        put_html(
                            '<h6 align="center">💡 Please try with a different keyword</h6>')
                        continue

                    put_html(f"""
                    <h2 align="center">🔍 Found {len(products)} results for <i>"{search}"</i>...</h2>
                    """)

                    # Display the final result in a table
                    put_table(
                        # tdata=generate_table_data(products),
                        # header=generate_table_header(),
                    )
