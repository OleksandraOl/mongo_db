from atlas_client import AtlasClient

def test_atlas_client_connection_is_successful():
    new_connection = AtlasClient()

def test_atlas_client_get_collection():
    new_connection = AtlasClient()
    collection = new_connection.get_collection()

    assert collection.name == "expenses"