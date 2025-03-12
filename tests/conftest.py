import pytest
import requests

from pyawx.auth import Auth, BasicAuth, OAuth2
from pyawx.http import HTTP


@pytest.fixture
def session() -> requests.Session:
    return requests.Session()


@pytest.fixture
def basic_auth() -> BasicAuth:
    return BasicAuth("user", "password")


@pytest.fixture
def oauth2() -> OAuth2:
    return OAuth2("token")


class MockAuth(Auth):
    def apply(self, session) -> None:
        pass


@pytest.fixture
def http() -> HTTP:
    auth = MockAuth()
    return HTTP("https://api.example.com", "v1", auth, verify_tls=True)
