from httpx import Client
from api_integrations.github_service import GithubService
from config import config


class TestAuth:

    def test_add_issue(self, get_http_client: Client):
        payload = {
            "title": "Found a bug",
            "body": "I'\''m having a problem with this.",
            "assignees": [config.TEST_USERNAME],
            "labels": ["bug"]
        }
        service = GithubService(get_http_client)
        response = service.create_issue(
            owner=config.TEST_USERNAME,
            repo=config.TEST_REPO,
            payload=payload
        )
        assert response.status_code == 201, f'{response.text}'
        checking_response = service.get_issues(
            owner=config.TEST_USERNAME,
            repo=config.TEST_REPO,
        )
        assert checking_response.json() != []

    def test_add_issue_negative(self, get_http_client: Client):
        payload = {
            "body": "I'\''m having a problem with this.",
            "assignees": [config.TEST_USERNAME],
            "milestone": None,
            "labels": ["bug"]
        }
        service = GithubService(get_http_client)
        response = service.create_issue(
            owner=config.TEST_USERNAME,
            repo=config.TEST_REPO,
            payload=payload
        )
        assert response.status_code == 422, f'{response.text}'
