import requests

def test_public_api_reachable():
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "id" in data and data["id"] == 1
