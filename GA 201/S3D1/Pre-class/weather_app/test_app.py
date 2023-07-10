import json
import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather_existing_city():
    client = app.test_client()
    response = client.get('/weather/Austin')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['temperature'] == 32
    assert data['weather'] == 'Hot'


def test_get_weather_nonexistent_city():
    client = app.test_client()
    response = client.get('/weather/Unknown')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['error'] == 'City not found'


def test_add_weather():
    data = {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Cloudy',
    }
    client = app.test_client()
    response = client.post('/weather', json=data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Weather data for Chicago added successfully'
    assert data['data'] == {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Cloudy',
    }


def test_add_weather_missing_fields():
    data1 = {
        'city': 'Houston',
        'temperature': 28,
        # missing 'weather' field
    }
    data2 = {
        'city': 'Houston',
        # missing 'temperature' field
        'weather': 'Cloudy'
    }

    client = app.test_client()

    response1 = client.post('/weather', json=data1)
    data1 = json.loads(response1.data)

    response2 = client.post('/weather', json=data2)
    data2 = json.loads(response2.data)

    assert response1.status_code == 400
    assert data1['message'] == 'Error, Invalid data!'

    assert response2.status_code == 400
    assert data2['message'] == 'Error, Invalid data!'


def test_update_weather():
    data = {'temperature': 34}

    client = app.test_client()
    response = client.put('/weather/Austin', json=data)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Weather data for Austin updated successfully'
    assert data['data'] == {
        'city': 'Austin',
        'temperature': 34,
        'weather': 'Hot'
    }


def test_update_weather_nonexistent_city():
    data = {'temperature': 30}

    client = app.test_client()
    response = client.put('/weather/Unknown city', json=data)
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Unknown city not found!'


def test_delete_weather():
    client = app.test_client()
    response = client.delete('/weather/Seattle')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Weather data for Seattle deleted successfully'


def test_delete_weather_nonexistent_city():
    client = app.test_client()
    response = client.delete('/weather/Unknown city')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Unknown city not found!'
