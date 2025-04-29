def get_item(collection, key):
    return collection[key]

def create_item(collection, key, value):


    
    if key in collection:
        raise ValueError("Key already exists")
    collection[key] = value
    return collection