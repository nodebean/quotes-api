from . import client


def test_fml_random():
    response = client.get("/api/fml/random")
    assert response.status_code == 200
    assert response.json()['text'] is not None
    assert response.json()['your_life_sucks'] is not None
    assert response.json()['you_deserved_it'] is not None