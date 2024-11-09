from flask_login import current_user


def test_not_login_required(client):
    response = client.get("/")
    assert response.status_code == 200
    hellow_message = client.get("/api/hello")
    assert hellow_message.status_code == 200
    assert hellow_message.json["message"] == "Hello, Flask"
