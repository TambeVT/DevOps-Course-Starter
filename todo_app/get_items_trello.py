import requests
import dotenv
import os
dotenv.load_dotenv()

reqUrl = "https://trello-proxy.azure-api.net/1/boards/6575b1e0697c0c91113c2035/lists"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "cards": "open",
    "card_fields": "id,name"  
}





response = requests.get(reqUrl, params= query_params)
response_json = response.json()

cards = []

for trello_list in response_json:
    for card in trello_list["cards"]:
        cards.append(card)


print(cards)