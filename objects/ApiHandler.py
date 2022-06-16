from dotenv import load_dotenv
import json
import requests
from objects.JSONParser import JSONParser
from bs4 import BeautifulSoup
import pandas as pd

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

NPCS = set([
    'alex', 'elliot', 'harvery', 'sam', 'sebastian', 'shane', 'abigail', 'emily', 'haley',
    'leah', 'maru', 'penny', 'caroline', 'clint', 'demetrius', 'dwarf', 'evelyn', 'george',
    'gus', 'jas', 'jodi', 'kent', 'krobus', 'lewis', 'linus', 'marnie', 'pam', 'pierre',
    'robin', 'sandy', 'vincent', 'willy', 'wizard'
    ])

##Handles calls to the MediaWiki API. Returns either requested string data or list of data.

class ApiHandler:


    #This function queries a pages description using the searched value.
    #calls jsonparser to get the summary information
    async def _get_summary_wikitext_(searched):
        searched = ApiHandler.replace_spaces(searched)
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=0&page={searched}&format=json").json()
        print(json.dumps(requested_JSON, indent=2))
        return requested_JSON['parse']['properties'][len(requested_JSON['parse']['properties'])-1]['*']
        #return json.dumps(requested_JSON, indent=2)
    

    #This function queries for members of a category and returns the list of members.
    async def _get_category_members_(category):
        category = ApiHandler.replace_spaces(category)
        requested_JSON = requests.get(f"{ENDPOINT}action=query&list=categorymembers&cmtitle=Category:{category}&cmlimit=500&format=json").json()
        members = JSONParser.get_queried_members(requested_JSON)
        return members


    ##returns the NPC's relationship section as wikitext.
    async def _get_NPC_relationships_(npc):
        if (npc.lower() in NPCS):
            requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=2&page={npc}&format=json").json()
            return JSONParser.get_parsed_wikitext(requested_JSON)
        else: 
            return "No such NPC."


    ##returns the NPC's schedule section wikitext.
    async def _get_NPC_schedule_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page={npc}&format=json").json()
        html = requested_JSON['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        df = pd.read_html(html)
        print(df)
        return 

   ###returns NPC's loved items as a string.
    async def _get_NPC_loves_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=4&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'loves', npc)


    ###returns NPC's loved items as a string.
    async def _get_NPC_likes_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=5&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'likes', npc)


    ###returns NPC's neutral items as a string.
    async def _get_NPC_neutrals_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=6&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'is neutral towards', npc)

   ###returns NPC's disliked items as a string.
    async def _get_NPC_dislikes_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=7&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'dislikes', npc)


   ###returns NPC's loved items as a string.
    async def _get_NPC_hates_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=8&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'hates', npc)


    ##returns the NPC's heart events section wikitext.
    async def _get_NPC_hearts_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=10&page={npc}&format=json").json()
        html = requested_JSON['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        df = pd.read_html(html)
        print(df)

    def replace_spaces(content):
        return content.replace(' ', '%20')