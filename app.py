import os

import sentry_sdk
import tornado.ioloop
import tornado.options
import tornado.web
from pywebio.platform.tornado import webio_handler as ws_webio_handler
from sentry_sdk.integrations.tornado import TornadoIntegration
from tornado.options import define, options

from src.handlers import feedback, index, privacy, terms,lang
from src.settings import ALLOWED_ORIGINS, ENVIRONMENT, RECONNECT_TIMEOUT, SENTRY_DSN, STATIC

define('port', default=8080, help='Run on the given port', type=int)
define('debug', default=False, help='Run on the debug mode', type=bool)


sentry_sdk.init(
    dsn=SENTRY_DSN,
    environment=ENVIRONMENT,
    integrations=[TornadoIntegration()],
)


class FourOhFourHandler(tornado.web.RequestHandler):
    """Page not found 404 handler"""

    def get(self, slug: str) -> None:
        del slug  # Unused
        self.render('src/templates/404.html')


def main() -> None:
    """Main entrypoint of the app"""
    tornado.options.parse_command_line()

    settings = dict(
        site_title='youtube auto publish',
        debug=options.debug,
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        static_url_prefix=STATIC,
    )

    app = tornado.web.Application(
        [
            (r'/', ws_webio_handler(lang, reconnect_timeout=RECONNECT_TIMEOUT,
                                    allowed_origins=ALLOWED_ORIGINS)),
            #     (r'/terms', http_webio_handler(terms)),
            #     (r'/privacy', http_webio_handler(privacy)),
            #     (r'/feedback', http_webio_handler(feedback)),
            (r'/([^/]+)', FourOhFourHandler),
        ], **settings
    )
    # if options.port == '':
    app.listen(5000)
    # else:
    # app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
