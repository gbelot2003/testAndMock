import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('config.TestConfig')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200