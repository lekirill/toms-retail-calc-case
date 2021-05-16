import pytest

from app import app as application
from app import clients


@pytest.fixture
def test_app():
    clients.setup(application)
    with application.test_client() as client:
        clients.setup(client)
        yield client
