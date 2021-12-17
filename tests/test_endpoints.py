import json
import time

def test_not_ready(app, client):
    response = client.get('/status/ready')
    assert response.status_code == 500
    expected = {"ready": False}
    assert expected == json.loads(response.get_data(as_text=True))

def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200
    expected = 'Hello world'
    assert expected == response.get_data(as_text=True)

def test_alive(app, client):
    response = client.get('/status/alive')
    assert response.status_code ==200
    expected = ''
    assert expected ==response.get_data(as_text=True)

def test_ready(app, client):
    time.sleep(10)
    response = client.get('/status/ready')
    assert response.status_code == 200
    expected = {"ready": True}
    assert expected == json.loads(response.get_data(as_text=True))