from flask_login import current_user


def test_login_required(client):
    response = client.get("/")
    assert response.status_code == 200
    response = client.get("/login-required")
    assert response.status_code == 401
    
    response = client.get("/login")
    assert response.status_code == 200
    
    response = client.get("/login-required")
    assert response.status_code == 200
    
    response = client.get("/logout")
    assert response.status_code == 200
    
    response = client.get("/login-required")
    assert response.status_code == 401
