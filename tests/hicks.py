from . import client

def test_hicks_by_id():
    response = client.get("/api/hicks/id/55")
    assert response.status_code == 200
    assert response.json()['quote'] == "Laughter is one of the greatest therapies."

def test_hicks_by_id_exception():
    response = client.get("/api/hicks/id/999")
    assert response.status_code == 404
    assert response.json()['detail'] == "Quote Not Found"

def test_hicks_random():
    response = client.get("/api/hicks/random")
    assert response.status_code == 200
    assert response.json()['id'] > 0

def test_hicks_count():
    response = client.get("/api/hicks/count")
    assert response.status_code == 200
    assert response.json()['count'] > -1

def test_hicks_all():
    response = client.get("/api/hicks/all")
    assert response.status_code == 200
    assert response.json()[55]['quote'] ==  "Laughter is one of the greatest therapies."
