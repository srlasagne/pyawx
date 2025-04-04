import pytest
import responses

from pyawx.resources.adapter import Adapter
from tests.conftest import MockModel


@responses.activate
def test_fetch_resource(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": [{"id": "123", "name": "test_resource"}]},
        status=200,
    )
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/123/",
        json={"id": "123", "name": "test_resource"},
        status=200,
    )

    result: dict = adapter.fetch("test_resource")
    assert result == {"id": "123", "name": "test_resource"}


@responses.activate
def test_create_resource(adapter: Adapter) -> None:
    responses.add(
        responses.POST,
        "https://api.example.com/api/v1/resource/",
        json={"id": "123", "name": "new_resource"},
        status=201,
    )

    payload = MockModel(name="new_resource")
    result: dict = adapter.create(payload)
    assert result == {"id": "123", "name": "new_resource"}


@responses.activate
def test_update_resource(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": [{"id": "123", "name": "existing_resource"}]},
        status=200,
    )
    responses.add(
        responses.PATCH,
        "https://api.example.com/api/v1/resource/123/",
        json={"id": "123", "name": "updated_resource"},
        status=200,
    )

    payload = MockModel(name="updated_resource")
    result: dict = adapter.update("existing_resource", payload)
    assert result == {"id": "123", "name": "updated_resource"}


@responses.activate
def test_delete_resource(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": [{"id": "123", "name": "resource_to_delete"}]},
        status=200,
    )
    responses.add(
        responses.DELETE,
        "https://api.example.com/api/v1/resource/123/",
        status=204,
    )

    result: None = adapter.delete("resource_to_delete")
    assert result is None


@responses.activate
def test_exists_resource(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": [{"id": "123", "name": "existing_resource"}]},
        status=200,
    )
    assert adapter.exists("existing_resource") is True


@responses.activate
def test_exists_resource_not_found(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": []},
        status=200,
    )
    assert adapter.exists("missing_resource") is False


@responses.activate
def test_get_id_by_name(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": [{"id": "123", "name": "test_resource"}]},
        status=200,
    )

    resource_id: str = adapter._get_id_by_name("test_resource")
    assert resource_id == "123"


@responses.activate
def test_get_id_by_name_not_found(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/resource/",
        json={"results": []},
        status=200,
    )

    with pytest.raises(
        ValueError, match="Resource with name 'non_existent' not found."
    ):
        adapter._get_id_by_name("non_existent")


@responses.activate
def test_names_to_ids(adapter: Adapter) -> None:
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/inventories/",
        json={"results": [{"id": "1", "name": "inventory_name"}]},
        status=200,
    )
    responses.add(
        responses.GET,
        "https://api.example.com/api/v1/projects/",
        json={"results": [{"id": "2", "name": "project_name"}]},
        status=200,
    )

    data: dict[str, str] = {
        "inventory": "inventory_name",
        "project": "project_name",
    }

    result: dict = adapter._names_to_ids(data)
    assert result == {
        "inventory": "1",
        "project": "2",
    }
