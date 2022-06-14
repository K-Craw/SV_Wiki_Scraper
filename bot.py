import os
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
    request_url = f"https://stardewvalleywiki.com/mediawiki/api.php?action=query&list=categorymembers&cmtitle=Category:Shops"
    requested_JSON = requests.get(request_url).json()
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('wiki!'):
        wikiTitle = message.content.split(' ')[1]
        stringify(wikiTitle)
        result = await pageHandler._get_summary(wikiTitle)
        await message.channel.send(result)

def stringify(content):
    content.replace(" ", "%20")


client.run(TOKEN)
