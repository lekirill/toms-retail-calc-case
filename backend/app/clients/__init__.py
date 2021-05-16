import settings
from .db import DBClient


def setup(app):
    app.db = DBClient(settings.DB_URL)
    app.db.setup()
