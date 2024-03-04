import pandas as pd
import requests
import json
from colorama import*

with open('competitor_list.json','r') as file:
    competitor_list=json.load(file).get('competitor_list')
    
# searchterm=input('enter the item to search :')
# searchterm=searchterm.lower()

for competetor in competitor_list:
    print(Style.BRIGHT+Fore.GREEN+competetor.get('name'))
    cookie=competetor.get('cookie')
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': cookie    }
            
    URL=competetor.get('store_api')
    responses=requests.get(URL,headers=HEADERS)
    data=responses.json()
    # print(data)
    items=data.get('items')
    for category in items:
        #  for category in items.get('categories'):
                print(Style.BRIGHT+Fore.YELLOW+category.get('name'))
    