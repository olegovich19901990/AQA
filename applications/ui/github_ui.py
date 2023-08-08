from applications.ui.pages.page_login import PageLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GitHubUI:

    def __init__(self,base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

        self.login_page = PageLogin(self.driver, self.base_url)
    
    def login(self, username, userpassword):
        return self.login_page.login(username, userpassword)
    
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
    
        