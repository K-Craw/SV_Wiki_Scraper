import json
import re
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

SEASONS = ['spring', 'summer', 'fall', 'winter']

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
OTHERS = ['Raining', 'Regular', 'Schedule']


##Handles calls to the MediaWiki API. Returns either requested string data or list of data.

class ApiHandler:

#-----------------------------------------SUMMARY----------------------------------------------------------------------------------
#These functions deal with general wiki queryings.
    #This function queries a pages description using the searched value.
    #calls jsonparser to get the summary information
    async def _get_summary_wikitext_(searched):
        searched = ApiHandler.replace_spaces(searched)
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=0&page={searched}&format=json").json()
        return requested_JSON['parse']['properties'][len(requested_JSON['parse']['properties'])-1]['*']
        #return json.dumps(requested_JSON, indent=2)
    
#-----------------------------------------LIST----------------------------------------------------------------------------------
#This function deals with categories querying.
    #This function queries for members of a category and returns the list of members.
    async def _get_category_members_(category):
        category = ApiHandler.replace_spaces(category)
        requested_JSON = requests.get(f"{ENDPOINT}action=query&list=categorymembers&cmtitle=Category:{category}&cmlimit=500&format=json").json()
        members = JSONParser.get_queried_members(requested_JSON)
        return members

#--------------------------------------RLEATIONSHIPS---------------------------------------------------------------------------------------

    ##returns the NPC's relationship section as wikitext.
    async def _get_NPC_relationships_(npc):
        if (npc.lower() in NPCS):
            requested_JSON = requests.get(f"{ENDPOINT}action=parse&prop=wikitext&section=2&page={npc}&format=json").json()
            return JSONParser.get_parsed_wikitext(requested_JSON)
        else: 
            return "No such NPC."

#---------------------------------------SCHEDULE------------------------------------------------------------------
#These functions deal with NPC schedules.
    ##returns the NPC's schedule section wikitext.
    async def _get_NPC_schedule_(npc, season):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page={npc}&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]

        for data in df:
            keys = data.keys()
            if ApiHandler.contains(keys, season):
                text = data[season][0]
            
        returnString = ApiHandler.parse_timetable(text)
        print(returnString)
        return returnString
        return "No such NPC/season. Check your command."

#----------------------------------------GIFTS-------------------------------------------------------------
#These methods return lists of NPCs gifts at different levels of preference.
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


   ###returns NPC's hated items as a string.
    async def _get_NPC_hates_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&page={npc}&section=8&format=json").json()
        return JSONParser.parse_gifts(requested_JSON, 'hates', npc)

#--------------------------------------HEARTS-------------------------------------------------------------------------------------

    ##returns the NPC's heart events section wikitext.
    async def _get_NPC_hearts_wikitext_(npc):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=10&page={npc}&format=json").json()
        html = requested_JSON['parse']['text']['*']
        soup = BeautifulSoup(html, 'html.parser')
        df = pd.read_html(html)
        print(df)

#--------------------------------------MISC------------------------------------------------------------------------------------

    def replace_spaces(content):
        return content.replace(' ', '%20')

    def contains(keys, target):
        for key in keys:
            if key == target:
                return True
        return False

    def parse_timetable(text):
        splitText = text.split()
        returnString = ""

        first = True
        for word in splitText:
            if (ApiHandler.contains(OTHERS, word) and first) or (ApiHandler.contains(WEEKDAYS, word) and first):
                returnString += word.upper() 
                first = False
            elif (ApiHandler.contains(OTHERS, word) and first) or (ApiHandler.contains(WEEKDAYS, word) and not first):
                returnString += "\n" + word.upper()
            elif word == 'Time' or word == 'Location':
                None
            elif word[0].isnumeric() and len(word) > 2:
                returnString += '\n\t\t-' + word
            else: 
                returnString += " " + word
        return returnString