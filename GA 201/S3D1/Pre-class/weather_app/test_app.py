import json
import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather_existing_city(client):
    response = client.get('/weather/New York')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['temperature'] == 20
    assert data['weather'] == 'Sunny'


def test_get_weather_nonexistent_city(client):
    response = client.get('/weather/Unknown')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['error'] == 'City not found'
