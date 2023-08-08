from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PageLogin:

    def __init__(self, driver, base_url) -> None:
        self.driver = driver
        self.login_url = base_url + '/login'

    @property
    def login_field(self):
        # 1 wait and find
        # 2 validate field
        return self.driver.find_element(By.ID, "login_field")

    @property
    def pass_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_btn(self):
        return self.driver.find_element(By.NAME, "commit")
    
    @property
    def sign_up_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Create an account")
    
    def navigate(self):
        self.driver .get (self.login_url)

    # Login method    

    def login(self, username, password):
        self.navigate()    

        self.login_field.send_keys(username)
        self.pass_field.send_keys(password)

        self.login_btn.click()
        
        if self.is_login_ok():
            return  True
        
        return False

    def proceed_to_signup_page(self):
        self.sign_up_link.click()

    # validation

    def is_login_ok(self):
        return self.driver.title != "Sign in to GitHub"
        

    #def is_login_error(self):
        #validation happens if user logged in or not
    #    return True