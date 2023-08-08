import os 

class UsersProvider:
    
    @staticmethod
    def fake_user():
        return {
            'login': 'olegovich19901990@gmail.com',
            'id': 'some_id',
            'password': 'December2023!'
        }
    
    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': '2'
        }
    
    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
            'id': os.environ.get("EXISTING_GITHUB_USER_ID")
        }
    