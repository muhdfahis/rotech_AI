import pandas as pd
import numpy as np
import requests
from colorama import 
import json

with open ('competitor_list.json','r') as file:
    competitor_list= json.load(file).get("competitor_list")
    
row_data={}
for competitor in competitor_list:
    row_data.update({competitor.get("name"):[]})
    
    
    
    for category in competitor_list:
        print(Fore.GREEN+ "Feching data from"+ competitor.get("name")+"......")
        URL = competitor.get("cat_url")
        cookie= competitor.get("cookie")
        HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': cookie    }
        
        
