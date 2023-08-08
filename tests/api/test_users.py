from providers.data.users_provider import UsersProvider
import requests
import pytest
 

def test_http_status_code200(github_api_client):
    r = requests.get('https://api.github.com/zen')

    assert r.status_code == 200

def test_user_exists(github_api_client):
    user_provider = UsersProvider()
    user = user_provider .existing_user_from_env()
    
    api_user = github_api_client.get_user(user['login'])

    assert user['login'] == user['login']
    assert user['id'] == user['id']

def test_user_non_exist(github_api_client):
    user = UsersProvider.fake_user()

    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])

        
    
 





