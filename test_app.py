import pytest

from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_get(client):
    resp = client.get('/')
    assert resp.data == b'<p>Hello, World</p>'


def test_get_json(client):
    resp = client.get('/', headers={'Accept': 'application/json'})
    assert resp.get_json() == {"message": "Good morning"}


def test_post(client):
    resp = client.post('/')
    assert resp.data == b'<p>Hello, World</p>'


def test_post_no_json(client):
    resp = client.post('/', headers={'Accept': 'application/json'})
    assert resp.data == b'<p>Hello, World</p>'
