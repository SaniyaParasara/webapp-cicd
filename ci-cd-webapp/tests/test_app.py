import json
from app import app

def test_healthz_ok():
    client = app.test_client()
    res = client.get('/healthz')
    assert res.status_code == 200
    data = json.loads(res.data.decode())
    assert data.get('status') == 'ok'

def test_home_ok():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    assert 'CI/CD Python Web App' in html or 'CI/CD PyWebApp' in html
