import os
import json
import requests
import discord
from dotenv import load_dotenv

from objects.pageHandler import pageHandler

load_dotenv()
TOKEN = os.getenv('TOKEN')
SVWIKI = os.getenv('SVWIKI')

#retrieves an API response from the mediawiki endpoint
#creates a client at the discord endpoint.
client = discord.Client()

#waits for client to run 
@client.event
async def on_ready():
    pagehandler = pageHandler()
    titles = await pageHandler.get_pages_search('Blacksmith')
    print(titles)


client.run(TOKEN)
