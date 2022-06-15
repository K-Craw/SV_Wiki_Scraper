from dotenv import load_dotenv
import json
import requests
from objects.JSONParser import JSONParser


##Handles calls to the MediaWiki API. Returns either requested string data or list of data.

class ApiHandler:
    #This function queries a pages description using the searched value.
    #calls jsonparser to get the summary information
    async def _get_summary(searched):
        searched = replace_spaces(searched)
        requested_JSON = requests.get(f"https://stardewvalleywiki.com/mediawiki/api.php?action=parse&page={searched}&format=json").json()
        summary = JSONParser.page_description(requested_JSON)
        return summary
    
    #This function queries for members of a category
    async def _get_category_members(category):
        json_request = requests.get(f"https://stardewvalleywiki.com/mediawiki/api.php?action=query&list=categorymembers&cmtitle=Category:{category}&cmlimit=500&format=json").json()
        members = JSONParser.get_category_members(json_request)
        return members

def replace_spaces(content):
    return content.replace(" ", "%20")