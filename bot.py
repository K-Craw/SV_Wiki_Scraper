import os

import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

#retrieves an API response from the mediawiki endpoint
response_API = requests.get('https://stardewvalleywiki.com/mediawiki/api.php?action=query&prop=revisions&titles=Blacksmith&rvslots=*&rvprop=content&formatversion=2')
print(response_API.content)

#creates a client at the discord endpoint.
client = discord.Client()

#waits for client to run 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
