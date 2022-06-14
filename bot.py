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
    print('online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('wiki!'):
        command = message.content.split(' ')[1]
        if command == 'NPCs':
            npcs = await pageHandler._get_list_of("NPCs")
            npcString = "The NPCs in the wiki are:"
            for npc in npcs:
                npcString += ' ' + npc['title'] + ','
            await message.channel.send(npcString)
        else: 
            wikiTitle = stringify(wikiTitle)
            result = await pageHandler._get_summary(wikiTitle)
            await message.channel.send(result)

def stringify(content):
    return content.replace(" ", "%20")


client.run(TOKEN)
