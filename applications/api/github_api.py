import requests

class GitHubAPI:
                       #domain
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_user(self, username: str):
        r = requests.get(f"{self.base_url}/users/{username}")
        r.raise_for_status()
        # above /\does this code
        #if r.status_code != 200:
        #  raise HTTPError

        return r.json()
    
    def get_repos(self, repos_serch_param: str):
        r = requests.get(
            f"{self.base_url}/serch/repositories?q={repos_serch_param}", 
            #params={'q': repos_serch_param}
            )
        r.raise_for_status()

        return r.json()