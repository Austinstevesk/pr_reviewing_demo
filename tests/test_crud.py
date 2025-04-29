import pytest

from src.testing_fastapi.crud import get_item, create_item

items = {"foo": {"name": "Foo", "description": "A test item"}}

def test_get_item():
    item = get_item(items, "foo")
    assert item["name"] == "Foo"
    assert item["description"] == "A test item"

def test_get_item_not_found():
    with pytest.raises(KeyError):
        get_item(items, "bar")

def test_create_item():
    new_item = {"name": "Bar", "description": "Another test item"}
    create_item(items, "bar", new_item)
    assert "bar" in items
    assert items["bar"] == new_item

def test_create_item_already_exists():
    with pytest.raises(ValueError):
        create_item(items, "foo", {"name": "Foo", "description": "Duplicate item"})