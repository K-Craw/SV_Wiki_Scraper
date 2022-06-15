import re
from dotenv import load_dotenv
import json
import requests
from objects.JSONParser import JSONParser



class MesssageHandler:
    #This function queries a pages description using the searched value.
    #calls jsonparser to get the summary information
    async def _get_summary(searched):
        requested_JSON = requests.get(f"https://stardewvalleywiki.com/mediawiki/api.php?action=parse&page={searched}&format=json").json()
        summary = JSONParser.page_description(requested_JSON)
        return summary
    
    async def _get_list_of(category):
        json_request = requests.get(f"https://stardewvalleywiki.com/mediawiki/api.php?action=query&list=categorymembers&cmtitle=Category:{category}&cmlimit=500&format=json").json()
        members = JSONParser.get_category_members(json_request)
        return members