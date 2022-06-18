import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
OTHERS = set(['Regular', 'Schedule', 'Rainy', 'Day'])

'''

Need to implement 'regular schedule' returned when a day with no info is requested.

'''



class SamHandler:

#----------------------------------SCHEDULE----------------------------------------------------------------
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=lewis&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]

        for data in df:
            keys = data.keys()
            if ApiHandler.contains(keys, season):
                text = data[season][0]
        
        print(text + '\n\n')
        returnString = SamHandler.parse_currentWeekday(text, weekday.lower())
        print(returnString)
        return returnString
        return "No such NPC/season. Check your command."

    def parse_currentWeekday(text, weekday):
        splitText = text.split()
        returnString = ""

        lastSeen = False
        first = True
        for word in splitText:

            if word.lower() == weekday and first:
                lastSeen = True
                returnString += word.upper()
                first = False

            elif word.lower() == weekday and not first:
                lastSeen = True
                returnString += '\n' + word.upper()

            elif word in WEEKDAYS and word.lower() != weekday:
                lastSeen = False

            elif lastSeen:

                if word[0].isnumeric() and word[2] == ':' or word[1] == ':':
                    returnString += '\n\t\t-' + word
                elif word == 'Time' or word == 'Location':
                    None
                else: 
                    returnString += " " + word

            else:
                None

        return returnString
#--------------------------------------------------------------------------------------------------------