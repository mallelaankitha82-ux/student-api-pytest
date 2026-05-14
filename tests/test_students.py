def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200