def get_item(collection, key):
    if key not in collection:
        raise KeyError("Item does not exist")
    return collection[key]


def create_item(collection, key, value):
    if key in collection:
        raise ValueError("Key already exists")
    collection[key] = value
    return collection
