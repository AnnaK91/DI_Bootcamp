import requests
import time

token = "1536409434:AAFBN93GyPXmdgM8DtM_bXo2TgfbD1-1_sc"


current_id = 0

def get_messages(offset):
    get_updates = f"https://api.telegram.org/bot{token}/getUpdates"
    r = requests.get(get_updates, params={"offset": offset+1}) # Making a request

    return r.json() # Converts the response to a dictionary

print(get_messages(0))

def send_message(destination, text)
    