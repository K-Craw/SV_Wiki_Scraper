from dotenv import load_dotenv
import json
import requests
from objects.JSONParser import JSONParser

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

##Handles calls to the MediaWiki API. Returns either requested string data or list of data.

class ApiHandler:
    #This function queries a pages description using the searched value.
    #calls jsonparser to get the summary information

    async def _get_summary_wikitext_(searched):
        searched = ApiHandler.replace_spaces(searched)
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=0&prop=wikitext&page={searched}&format=json").json()
        return JSONParser.get_parsed_wikitext(requested_JSON)
    
    #This function queries for members of a category
    async def _get_category_members_(category):
        category = ApiHandler.replace_spaces(category)
        requested_JSON = requests.get(f"{ENDPOINT}action=query&list=categorymembers&cmtitle=Category:{category}&cmlimit=500&format=json").json()
        members = JSONParser.get_queried_members(requested_JSON)
        return members


    ##returns the NPC's relationship section wikitext.
    async def _get_NPC_relationships_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=2&page={npc}&format=json").json()
        return JSONParser.get_parsed_wikitext(requested_JSON)

    ##returns the NPC's schedule section wikitext.
    async def _get_NPC_schedule_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=1&page={npc}&format=json").json()
        return JSONParser.get_parsed_wikitext(requested_JSON)

    ##returns the NPC's gifts section wikitext.
    async def _get_NPC_gifts_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=3&page={npc}&format=json").json()
        return JSONParser.get_parsed_wikitext(requested_JSON)

    ##returns the NPC's heart events section wikitext.
    async def _get_NPC_hearts_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=10&page={npc}&format=json").json()
        return JSONParser.get_parsed_wikitext(requested_JSON)

    def replace_spaces(content):
        return content.replace(' ', '%20')