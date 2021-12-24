from . import client


def test_marx_by_id():
    response = client.get("/api/marx/id/108")
    assert response.status_code == 200
    assert response.json()['quote'] == "Machinery has greatly increased the number of well-to-do idlers."

def test_marx_by_id_exception():
    response = client.get("/api/marx/id/999")
    assert response.status_code == 404
    assert response.json()['detail'] == "Quote Not Found"

def test_marx_random():
    response = client.get("/api/marx/random")
    assert response.status_code == 200
    assert response.json()['id'] > 0

def test_marx_all():
    response = client.get("/api/marx/all")
    assert response.status_code == 200
    assert response.json()[107]['quote'] == "Machinery has greatly increased the number of well-to-do idlers."

def test_marx_count():
    response = client.get("/api/marx/count")
    assert response.status_code == 200
    assert response.json()['count'] > -1