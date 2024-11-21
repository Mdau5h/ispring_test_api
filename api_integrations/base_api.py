from httpx import Client, Request


class BaseApi:
    def __init__(self, base_url: str, client: Client, api_version: str, timeout: int = 15000):
        self.base_url = base_url
        self.headers = {
            'X-GitHub-Api-Version': api_version,
            'User-Agent': "Mdau5h's testing app"
        }
        self.client = client
        self.timeout = timeout

    def get_api_call(self, url: str, params=None):
        request = Request('GET', url=url, params=params, headers=self.headers)
        return self.client.send(request)

    def post_api_call(self, url: str, params):
        request = Request('POST', url=url, json=params, headers=self.headers)
        return self.client.send(request)

    def delete_api_call(self, url: str, params):
        request = Request('DELETE', url=url, json=params, headers=self.headers)
        return self.client.send(request)

    def put_api_call(self, url: str, params):
        request = Request('PUT', url=url, json=params, headers=self.headers)
        return self.client.send(request)

    def patch_api_call(self, url: str, params):
        request = Request('PATCH', url=url, json=params, headers=self.headers)
        return self.client.send(request)
