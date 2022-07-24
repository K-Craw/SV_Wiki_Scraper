Current Goal:
-Implment querying of NPCs
    - Change query so that it returns a list of the items instead of returning a string. This way the items
    could be used to handle data. Think with schedule: schedule can be handled and used to check where
    any NPC is at any time.
    
To be implemented/plans:
    -Need to fix errors with spacing.
    -need to come up with more complete/better system design.
            -requests for different forms of data from the ame page? e.g wiki Blacksmith could return the whole page,
            wiki blacksmith help could return all the sections on his page, wiki blacksmith process_geodes could
            return info from the process geodes section.
    -Need to figure out how to parse images.
    -Need to look more into design patterns.

Could implement?
    - Price check
    - Compare
    - Season check
    - Construction check
    - Likes/Dislikes (done)
    - Location @ date/time (almost done)
    - recipe checks
    - general wiki checks

----------------------------------------------------------------------------------------------------
Design:
Bot.py -> CommandHandler.py 
CommandHandler.py -> NPCHandler.py or ApiHandler.py
NPCHandler.py return or -> NPCSchedules
ApiHandler return.

----------------------------------------------------------------------------------------------------
Noted bugs:
    - Krobus does not return likes or other gifts correctly due to his section order.
    - Elliot's schedule almost works, skips random words on hearts with leah, like alex with haley.
        Also needs to return multiple, like where two fridays are included in multiple hearts with leah.
    - Robin's schedule doesn't return monday community centre restored + regular.

-----------------------------------------------------------------------------------------------------





    