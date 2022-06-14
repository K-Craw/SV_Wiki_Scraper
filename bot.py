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
    #if the message is the bot just ignore it
    if message.author == client.user:
        return

    #if the message is a command, checks to see what kind of command it is.
    #handles command.
    if message.content.startswith('wiki!'):
        command = message.content.split(' ')[1]
        if command == 'list':
            category = message.content.split(' ')
            items = await pageHandler._get_list_of(category)
            itemString = f"The {category} in the wiki are:"
            for item in items:
                itemString += ' ' + item['title'] + ','
            await message.channel.send(itemString)
        #current implementation of get description
        #needs to be changed.
        else: 
            wikiTitle = replace_spaces(command)
            result = await pageHandler._get_summary(wikiTitle)
            await message.channel.send(result)

#replaces spaces with %20 for URLs
def replace_spaces(content):
    return content.replace(" ", "%20")


client.run(TOKEN)
