import logging
from waitress import serve
from paste.translogger import TransLogger

import settings
from app import app, clients


def run_server():
    clients.setup(app)

    if settings.IS_PRODUCTION:
        # Production
        logger = logging.getLogger('waitress')
        logger.setLevel(logging.DEBUG)
        serve(TransLogger(app), host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
    else:
        # Development
        app.run(host=settings.SERVICE_HOST, port=settings.SERVICE_PORT, debug=settings.DEBUG)


if __name__ == '__main__':
    run_server()
