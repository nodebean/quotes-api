from . import client

def test_engels_by_id():
    response = client.get("/api/engels/id/29")
    assert response.status_code == 200
    assert response.json()['quote'] == "It is precisely the alteration of nature by men, not solely nature as such, which is the most essential and immediate basis of human thought."

def test_engels_by_id_exception():
    response = client.get("/api/engels/id/999")
    assert response.status_code == 404
    assert response.json()['detail'] == "Quote Not Found"

def test_engels_random():
    response = client.get("/api/engels/random")
    assert response.status_code == 200
    assert response.json()['id'] > 0

def test_engels_count():
    response = client.get("/api/engels/count")
    assert response.status_code == 200
    assert response.json()['count'] > -1

def test_engels_all():
    response = client.get("/api/engels/all")
    assert response.status_code == 200
    assert response.json()[28]['quote'] == "It is precisely the alteration of nature by men, not solely nature as such, which is the most essential and immediate basis of human thought."