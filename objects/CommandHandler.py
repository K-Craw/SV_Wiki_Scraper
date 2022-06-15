from objects.ApiHandler import ApiHandler

#CommandHandler handles the nitty-gritty of commands, calls the API to get the info for them, and returns the
#required message for the bot to send to the server.
class CommandHandler:

    #returns a string of items belonging to the category passed in.
    async def list_command(tokens):
        #adds all list arguments and then urlifys them for
        #processing
        category = ""
        for token in tokens:
            if (tokens.index(token) > 2):
                category += " " + token 
            elif (tokens.index(token) == 2):
                category += token

        items = await ApiHandler._get_category_members(category)

        itemString = f"The list of {category} in the wiki are:"
        for item in items:
            if (items.index(item) == len(items)-1):
                itemString += 'and ' + item['title']
            else:
                itemString += ' ' + item['title'] + ','

        return itemString

    async def summary_command(tokens):
        return await ApiHandler._get_summary(tokens[2])

    def help_command():
        return ('Here is a list of commands: \n' 
                + '\t- sum <page> to return a short summary of the page: Ex. $V Clint -> returns description of Clint.\n'
                + '\t- list <category> to list items in that category: Ex. $V list NPCs -> returns a list of all NPC names.')
    