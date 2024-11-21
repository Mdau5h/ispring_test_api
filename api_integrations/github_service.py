from api_integrations.base_api import BaseApi
from httpx import Client
from config import config


class GithubService(BaseApi):
    def __init__(self, client: Client):
        super().__init__(
            base_url=config.BASE_URL,
            client=client,
            api_version='2022-11-28'
        )
        self.headers['Authorization'] = f'Bearer {config.GITHUB_TOKEN}'

    def create_issue(self, owner: str, repo: str, payload: dict = None):
        url = f"/repos/{owner}/{repo}/issues"
        return self.post_api_call(f"{self.base_url}{url}", params=payload)

    def get_issues(self, owner: str, repo: str):
        url = f"/repos/{owner}/{repo}/issues"
        return self.get_api_call(f"{self.base_url}{url}")
