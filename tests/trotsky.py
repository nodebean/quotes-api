from . import client

def test_trotsky_by_id():
    response = client.get("/api/trotsky/id/56")
    assert response.status_code == 200
    assert response.json()['quote'] == "The Fascists find their human material mainly in the petty bourgeoisie. The latter has been entirely ruined by big capital. There is no way out for it in the present social order, but it knows of no other."

def test_trotsky_by_id_exception():
    response = client.get("/api/trotsky/id/999")
    assert response.status_code == 404
    assert response.json()['detail'] == "Quote Not Found"

def test_trotsky_random():
    response = client.get("/api/trotsky/random")
    assert response.status_code == 200
    assert response.json()['id'] > 0

def test_trotsky_count():
    response = client.get("/api/trotsky/count")
    assert response.status_code == 200
    assert response.json()['count'] > -1

def test_trotsky_all():
    response = client.get("/api/trotsky/all")
    assert response.status_code == 200
    assert response.json()[55]['quote'] ==  "The Fascists find their human material mainly in the petty bourgeoisie. The latter has been entirely ruined by big capital. There is no way out for it in the present social order, but it knows of no other."
