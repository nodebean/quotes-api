from . import client

def test_status_check():
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_health_check():
    response = client.get("/api/status/healthz")
    assert response.status_code == 200
    assert response.json() == {"health":"OK"}

def test_ready_check():
    response = client.get("/api/status/readyz")
    assert response.status_code == 200
    assert response.json() == {"ready":"true"}
