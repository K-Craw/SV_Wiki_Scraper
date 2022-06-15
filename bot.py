import os
import discord
from dotenv import load_dotenv
import requests
import json
from objects.ApiHandler import ApiHandler
from objects.CommandHandler import CommandHandler

load_dotenv()
TOKEN = os.getenv('TOKEN')
SVWIKI = os.getenv('SVWIKI')

#retrieves an API response from the mediawiki endpoint
#creates a client at the discord endpoint.
client = discord.Client()



#waits for client to run 
@client.event
async def on_ready():
    print(await ApiHandler._get_category_members_('NPCs'))


@client.event
async def on_message(message):
    #if the message is the bot just ignore it
    if message.author == client.user:
        return

    #if the message is a command, checks to see what kind of command it is.
    #handles command.
    elif is_command(message):
        # Get the token stream and the first argument for message routing
        tokens = message.content.split(' ')
        arg1 = tokens[1]

        if arg1 == 'list':
            await message.channel.send(await CommandHandler.list_command(tokens))
        
        elif arg1 == 'sum':
            await message.channel.send( await CommandHandler.summary_command(tokens))

        elif arg1 == 'help':
            await message.channel.send(CommandHandler.help_command())
        
    else: 
        return


def is_command(message):
    return message.content.startswith("$V")


client.run(TOKEN)
