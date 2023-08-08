import os 


class Config:
    base_url_api = os.environ.get("BASE_URL", 'https://api.github.com')
    base_url_ui = os.environ.get("BASE_URL", 'https://github.com')
     