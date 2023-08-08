#from selenium import webdriver
#from selenium.webdriver.common.keys import keys

from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from config.config import Config
from providers.data.users_provider import UsersProvider



def test_check_login(github_ui_client):
    user = UsersProvider.fake_user()
    
    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.login_page.is_login_ok()


