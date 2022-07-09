Current Goal:
-Implment querying of NPCs
    - Change query so that it returns a list of the items instead of returning a string. This way the items
    could be used to handle data. Think with schedule: schedule can be handled and used to check where
    any NPC is at any time.
-Implement querying NPC location at date/time
    - format: $V location <NPC> <Season> <Day> <Time>
    - $V location lewis Spring 19 11:30am
    - Probably going to have to parse this directly out of all the text contained within the correct table,
        since theres no easy way to query out what day/time each table refers to. Honestly easier to parse
        directly out of test since the text is formulaic.
        -formula: <day of week> Time Location <time> <location> <time> <location> .... <day of week> Time Location....
        Could parse the info out of this pretty easily.

NPCS THAT NEED SCHEDULE IMPLEMNTED:
    -All except abigail, lewis, penny, haley.
    
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
    - Location @ date/time
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
    - Sam and Abigail parse schedules incorrectly due to the regular schedule inclusion.
    - Penny's schedule handler parses the community center restored/not restored sections in winter incorrectly.
    - Haley's schedule handler parses the multi-day sections incorrectly.
    - Leah's normal schedule needs to return beach bridge repaired and not repaired.
    - Clint's schedule on friday when the community centre is restored doesn't get accessed.
    - Evelyn's schedule does not return community center repaired options.
    - George's schedule doesn't return his summer friday, will need to make an exception.
    - Gus's schedule doesn't return community center repaired tuesday.
    - Jas handler incomplete, page is really badly formatted on the wiki.
    - Alex's schedule returns wednesday's phrasing with "6 hearts with Haley" weirdly.

-----------------------------------------------------------------------------------------------------
SCHEDULE HANDLERS
 Alex -
 Abigail -
 Caroline -
 Clint -
 Demetrius
 Elliot
 Emily -
 Evelyn -
 George -
 Gus -
 Haley -
 Harvey
 Jas -
 Jodi -
 Kent
 Leah -
 Leo
 Lewis -
 Linus 
 Marnie
 Maru -
Pam
Penny -
Robin
Sam 
Sebastian
Shane
Vincent
Willy



    