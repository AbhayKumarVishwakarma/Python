from app import app


def test_hello():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello, World!'}


def test_login():
    client = app.test_client()
    response = client.post('/login', data={'email': 'abc@gmail.com', 'password': '12345'})

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Login successfully', 'submitted_email': 'abc@gmail.com',
                                   'submitted_password': '12345'}


def test_submit():
    client = app.test_client()
    response = client.post('/submit', data={'data': 'Hello, Flask'})

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Form submitted', 'submitted_data': 'Hello, Flask'}


def test_feedback_submission():
    client = app.test_client()

    response = client.post('/submit_feedback', data={'name': 'John Doe', 'message': 'Great app!'})

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Feedback submitted successfully'}

