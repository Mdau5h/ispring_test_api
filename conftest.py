import pytest
from httpx import Client


@pytest.fixture(scope='session')
def get_http_client():
    with Client() as client:
        yield client
