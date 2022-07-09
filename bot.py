import os
import discord
from dotenv import load_dotenv
from objects.BotCommandHandler import BotCommandHandler
from objects.NpcSchedules.DemetriusHandler import DemetriusHandler
from objects.NpcSchedules.ElliottHandler import ElliottHandler
from objects.NpcSchedules.HarveyHandler import HarveyHandler

load_dotenv()
TOKEN = os.getenv('TOKEN')
SVWIKI = os.getenv('SVWIKI')

#retrieves an API response from the mediawiki endpoint
#creates a client at the discord endpoint.
client = discord.Client()

#waits for client to run 
@client.event
async def on_ready():
    print(await HarveyHandler.get_schedule('Summer', 'Saturday'))
    print("Online!")
    await client.close()

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

        if (arg1 == 'list'):
            await message.channel.send( await BotCommandHandler.list_command(tokens) )
        
        elif (arg1 == 'sum'):
            await message.channel.send( await BotCommandHandler.summary_command(tokens) )
        
        elif (arg1 == 'loves'):
            await message.channel.send( await BotCommandHandler.loves_command(tokens) )

        elif (arg1 == 'likes'):
            await message.channel.send( await BotCommandHandler.likes_command(tokens) )

        elif (arg1 == 'neutral'):
            await message.channel.send( await BotCommandHandler.neutrals_command(tokens) )
        
        elif (arg1 == 'dislikes'):
            await message.channel.send( await BotCommandHandler.dislikes_command(tokens) )
        
        elif (arg1 == 'hates'):
            await message.channel.send( await BotCommandHandler.hates_command(tokens) )

        elif (arg1 == 'schedule'):
            await message.channel.send( await BotCommandHandler.schedule_command(tokens) )

        elif (arg1 == 'help'):
            await message.channel.send(BotCommandHandler.help_command())
        
        else:
            await message.channel.send("Invalid command.")
    else: 
        return


def is_command(message):
    return message.content.startswith("$V")


client.run(TOKEN)
