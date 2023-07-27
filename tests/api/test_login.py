import requests

def test_http_status_code200():
    r = requests.get('https://api.github.com/users\defunkt')
    print(r.__dict__)
    assert r.status_code == 200
    #assert r.text !== "Speak like a human."
