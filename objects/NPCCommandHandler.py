from bs4 import BeautifulSoup
import pandas as pd
from objects.ApiHandler import ApiHandler
import requests

NPCS = set([
    'alex', 'elliot', 'harvery', 'sam', 'sebastian', 'shane', 'abigail', 'emily', 'haley',
    'leah', 'maru', 'penny', 'caroline', 'clint', 'demetrius', 'dwarf', 'evelyn', 'george',
    'gus', 'jas', 'jodi', 'kent', 'krobus', 'lewis', 'linus', 'marnie', 'pam', 'pierre',
    'robin', 'sandy', 'vincent', 'willy', 'wizard'
    ])

#NPCCommandHandler performs initial checks on the NPCs and handles the API's reply.
class NPCCommandHandler:

#---------------------------------------------------------------------------------------------------------
#These commands handle NPC gift lists accoridng to likes and dislikes.

    #checks if the NPC is valid and returns their loves as a string if it is, 
    #if not returns no such giftable NPC.
    async def get_npc_loves(npc):
        if (npc.lower() in NPCS):
            loves = await ApiHandler._get_NPC_loves_(npc)
            return loves
        else:
            return 'no such giftable NPC'
    
    #checks if the NPC is valid and returns their likes as a string if it is, 
    #if not returns no such giftable NPC.
    async def get_npc_likes(npc):
        if (npc.lower() in NPCS):
            likes = await ApiHandler._get_NPC_likes_(npc)
            return likes
        else:
            return 'no such giftable NPC'

    #checks if the NPC is valid and returns their neutrals as a string if it is, 
    #if not returns no such giftable NPC.   
    async def get_npc_neutrals(npc):
        if (npc.lower() in NPCS):
            neutrals = await ApiHandler._get_NPC_neutrals_(npc)
            return neutrals
        else:
            return 'no such giftable NPC'

    #checks if the NPC is valid and returns their dislikes as a string if it is, 
    #if not returns no such giftable NPC.
    async def get_npc_dislikes(npc):
        if (npc.lower() in NPCS):
            dislikes = await ApiHandler._get_NPC_dislikes_(npc)
            return dislikes
        else:
            return 'no such giftable NPC'

    #checks if the NPC is valid and returns their hates as a string if it is, 
    #if not returns no such giftable NPC.       
    async def get_npc_hates(npc):
        if (npc.lower() in NPCS):
            hates = await ApiHandler._get_NPC_hates_(npc)
            return hates
        else:
            return 'no such giftable NPC'

#---------------------------------------------------------------------------------------------------------