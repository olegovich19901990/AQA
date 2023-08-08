from providers.data.repositories_provider import RepositoriesProvider


def test_check_repos_can_be_found(github_api_client):
    repo = RepositoriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert len['total_count'] !=0
    assert len(repos['items']) !=0

def test_check_repos_can_be_found(github_api_client):
    repo = RepositoriesProvider.non_existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert len['total_count'] == repo['total_count']
    assert len(repos['items']) == repo['total_count'] 
    
               


