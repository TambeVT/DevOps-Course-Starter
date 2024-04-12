import requests
import os
import dotenv

from todo_app.data.item import Item


dotenv.load_dotenv()

def get_items():
    key =  os.getenv("TRELLO_API_KEY")
    token =  os.getenv("TRELLO_API_TOKEN")
    conn ="trello-proxy.azure-api.net"


    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    response =requests.get ("https://trello-proxy.azure-api.net/1/boards/6575b1e0697c0c91113c2035/lists?key={}&token={}&cards=open&card_fields=id,name".format(key,token),headers= headersList)

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