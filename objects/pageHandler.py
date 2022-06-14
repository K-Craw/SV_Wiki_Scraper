import re
from dotenv import load_dotenv
import json
import requests
from objects.JSONParser import JSONParser



class pageHandler:
    def __init__(self):
        self = self

    #This function queries a pages description using the searched value.
    async def get_page_summary(searched):
        request_url = f"https://stardewvalleywiki.com/mediawiki/api.php?action=parse&page={searched}&section=0&format=json"
        request = requests.get(request_url).json()
        print(JSONParser.summary(request))  
        

