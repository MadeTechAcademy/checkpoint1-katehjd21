from app import app 

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Apprenticeship Duties" in response.data
    assert b"View all duties" in response.data
    assert b"Automate!" in response.data 

def test_all_duties(client):
    response = client.get("/all")
    assert response.status_code == 200
    assert b"All Duties" in response.data
    assert b"Duty 6" in response.data
    assert b"Duty 12" in response.data
    assert b"Implement a good coverage of monitoring" in response.data

def test_theme_page(client):
    response = client.get("/theme/4")
    assert response.status_code == 200
    assert b"Houston, Prepare to Launch" in response.data
    assert b"Duty 6" in response.data
    assert b"Implement and improve release automation" in response.data

def test_return__to_homepage_link_on_theme_page(client):
    response = client.get("/theme/6")
    assert b"Back to all themes" in response.data


