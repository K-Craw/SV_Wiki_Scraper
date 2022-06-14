import os
import discord
from dotenv import load_dotenv
import requests
import json
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
    list_of = requests.get(f"https://stardewvalleywiki.com/mediawiki/api.php?action=query&prop=categories&titles=Coop&format=json").json()
    print(json.dumps(list_of))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('wiki!'):
        command = message.content.split(' ')[1]
        if command == 'list':
            category = message.content.split(' ')[2]
            items = await pageHandler._get_list_of(category)
            itemString = f"The {category} in the wiki are:"
            for item in items:
                itemString += ' ' + item['title'] + ','
            await message.channel.send(itemString)

        else: 
            wikiTitle = stringify(command)
            result = await pageHandler._get_summary(wikiTitle)
            await message.channel.send(result)

def stringify(content):
    return content.replace(" ", "%20")


client.run(TOKEN)
