import requests

def test_http_status_code200():
    r = requests.get('https://api.github.com/users')
    print(r.__dict__)
    assert r.status_code == 200

def test_user_exists():
    r = requests.get('https://api.github.com/users/defunkt')
    print(r.__dict__)
    
    assert r.json()['login'] == 'defunkt'
    assert r.json()['id'] == 2

def test_user_non_existant():
    r = requests.get('https://api.github.com/users/eriufhieqtp84')
    print(r.__dict__)
    
    r.status_code == 404
    r.json()['message'] == 'Not founds'


