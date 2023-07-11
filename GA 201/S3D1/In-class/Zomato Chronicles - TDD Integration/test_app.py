from app import app


def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Welcome to Zomato Chronicles!'


def test_create_dish():
    client = app.test_client()
    response = client.post('/dishes/create', data={
        'id': '3',
        'name': 'Hot dog',
        'price': '99',
        'available': 'yes'
    })
    assert response.status_code == 302
    assert response.location == '/dishes'


def test_list_dishes():
    client = app.test_client()
    response = client.get('/dishes')
    data = response.data

    assert response.status_code == 200
    assert b'Pizza' in data
    assert b'Burger' in data


def test_update_dish():
    client = app.test_client()
    response = client.post('/dishes/update/3', data={
        'available': 'no'
    })
    assert response.status_code == 302
    assert response.location == '/dishes'

    response = client.get('/dishes')
    data = response.data

    assert response.status_code == 200
    assert b'no' in data


def test_delete_dish():
    client = app.test_client()
    response = client.get('/dishes/delete/3')

    assert response.status_code == 302
    assert response.location == '/dishes'

    response = client.get('/dishes')
    data = response.data

    assert response.status_code == 200
    assert b'Hot dog' not in data


def test_create_order():
    client = app.test_client()
    response = client.post('/orders/create', data={
        'orderId': '2',
        'customerName': 'Vikash',
        'dishId': '1',
        'status': 'delivered'
    })
    assert response.status_code == 302
    assert response.location == '/orders'


def test_update_order():
    client = app.test_client()
    response = client.post('/orders/update/2', data={
        'status': 'completed'
    })
    assert response.status_code == 302
    assert response.location == '/orders'

    response = client.get('/orders')
    data = response.data

    assert response.status_code == 200
    assert b'completed' in data


def test_list_orders():
    client = app.test_client()
    response = client.get('/orders')
    assert response.status_code == 200
    assert b'Ankit' in response.data
