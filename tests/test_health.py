def test_health_check(client):
    """
    Test that the health check endpoint returns the expected response.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
