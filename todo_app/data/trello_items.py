import requests
import os
import dotenv

from todo_app.data.item import Item


dotenv.load_dotenv()

def get_items():
    key =  os.getenv("TRELLO_API_KEY")
    token =  os.getenv("TRELLO_API_TOKEN")
    board_id =  os.getenv("TRELLO_BOARD_ID")


    response =requests.get("https://trello-proxy.azure-api.net/1/boards/{}/lists?key={}&token={}&cards=open".format(board_id, key,token))

    response_list =response.json()
    items=[]
    for trello_list in response_list:
        print(trello_list)
        for trello_card in trello_list['cards']:
            item = Item.from_trello_card(trello_card, trello_list)
            items.append(item)
    
    return items
    

def add_item(title):
    reqUrl = "https://trello-proxy.azure-api.net/1/cards"

    query_params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_TODO_LIST_ID"),
        "name": title
    }


    response = requests.post(reqUrl, params= query_params)

    print(response.text)

def move_item_to_done(item_id):
    
    reqUrl = f"https://trello-proxy.azure-api.net/1/cards/{item_id}"

    query_params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_DONE_LIST_ID"),
  }

    response = requests.put(reqUrl, params= query_params)

    response.raise_for_status()