from objects.ApiHandler import ApiHandler
from objects.NPCCommandHandler import NPCCommandHandler


#BotCommandHandler takes the tokens from the message send to the bot,
#checks if they match a valid format,
#and if they do it passes the npc to the NPCCommandHandler for API call handling.
class BotCommandHandler:

    async def schedule_command(tokens):
        if (len(tokens) > 4): return "Huh? This command doesn't exist.\nTry: $V schedule <npc name> <season>"
        npc = tokens[2]
        season = tokens[3]

        return await NPCCommandHandler.get_npc_schedule(npc, season)

#------------------------------------------------------------------------------
#These functions take an NPC and returns the gifts they like/dislikes/neutral/etc.
    #returns a list of items the given NPC loves.
    async def loves_command(tokens):
        if (len(tokens) > 3): return "Huh? This command doesn't exist.\nTry: $V loves/likes/neutral/dislikes/hates <npc name>"
        npc = tokens[2]

        return await NPCCommandHandler.get_npc_loves(npc)
        

    #returns a list of items the given NPC likes.
    async def likes_command(tokens):
        if (len(tokens) > 3): return "Huh? \nThis command doesn't exist.\nTry: $V loves/likes/neutral/dislikes/hates <npc name>"
        npc = tokens[2]

        return await NPCCommandHandler.get_npc_likes(npc)


    #returns a list of items the given NPC is neutral towards.
    async def neutrals_command(tokens):
        if (len(tokens) > 3): return "Huh? \nThis command doesn't exist.\nTry: $V loves/likes/neutral/dislikes/hates <npc name>"
        npc = tokens[2]

        return await NPCCommandHandler.get_npc_neutrals(npc)


    #returns a list of items the given NPC dislikes
    async def dislikes_command(tokens):
        if (len(tokens) > 3): return "Huh? \nThis command doesn't exist.\nTry: $V loves/likes/neutral/dislikes/hates <npc name>"
        npc = tokens[2]

        return await NPCCommandHandler.get_npc_dislikes(npc)
        

    #returns a list of items the given NPC hates
    async def hates_command(tokens): 
        if (len(tokens) > 3): return "Huh? \nThis command doesn't exist.\nTry: $V loves/likes/neutral/dislikes/hates <npc name>"
        npc = tokens[2]

        return await NPCCommandHandler.get_npc_hates(npc)

#------------------------------------------------------------------------------

    #returns a string of items belonging to the category passed in.
    async def list_command(tokens):
        
        #adds all list arguments and then urlifys them for
        #processing
        category = BotCommandHandler.replace_spaces(tokens)

        items = await ApiHandler._get_category_members_(category)

        itemString = f"The list of {category} in the wiki are:"
        for item in items:
            if (items.index(item) == len(items)-1):
                itemString += 'and ' + item['title']
            else:
                itemString += ' ' + item['title'] + ','

        return itemString


    #returns a summary of the page requested
    async def summary_command(tokens):
        return await ApiHandler._get_summary_wikitext_(tokens[2])


    #Returns a string explaining all commands available and how they are used.
    def help_command():
        return ('Here is a list of commands: \n' 
                + '\t- sum <page> to return a short summary of the page: Ex. $V Clint -> returns description of Clint.\n'
                + '\t- list <category> to list items in that category: Ex. $V list NPCs -> returns a list of all NPC names.\n'
                + '\t- loves/likes/neutrals/dislikes/hates <npc> to return a list of items at that NPCs given preference level: Ex: $V loves Clint -> returns list of items Clint loves.\n'
                + '\t- schedule <npc> <sesason> to return the NPCs schedule for each day of the given season. Ex: $V schedule lewis summer.'
                )

    def replace_spaces(tokens):
        tokenized = ""

        for token in tokens:
            if (tokens.index(token) > 2):
                tokenized += "%20" + token 
            elif (tokens.index(token) == 2):
                tokenized += token

        return tokenized