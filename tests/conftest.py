import pytest
import requests

from pyawx.auth import BasicAuth, OAuth2


@pytest.fixture
def session() -> requests.Session:
    return requests.Session()


@pytest.fixture
def basic_auth() -> BasicAuth:
    return BasicAuth("user", "password")


@pytest.fixture
def oauth2() -> OAuth2:
    return OAuth2("token")
