import os
from dotenv import load_dotenv, find_dotenv
import pytest
import requests
from todo_app import app
import mongomock


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(client):
    #arrange
    mongo_client = pymongo.mongoclient(os.getenv("MONGODB_CONNECTION_STRING"))

    db = client{os.getenv("MUNGO_DATABASE_NAME")}

    collection =db(os.getenv("MUNGODB_COLLECTION_NAME"))
    test_document ={
        "name": "Test Item",
        "status": "To Do"
    }

    collection.insert_one(test_document)

    # Act
    response = client.get('/')

    #Assert
    assert response.status_code == 200
    assert 'Test item' in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    def raise_for_status(self):
        pass

    def json(self):
        return self.fake_response_data

def stub(url, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')

    if f'https://trello-proxy.azure-api.net/1/boards/{test_board_id}/lists' in url:
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card'}]
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')
def test_fixture(client):
    assert True


