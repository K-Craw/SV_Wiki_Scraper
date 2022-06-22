import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])


class AbigailHandler:
#----------------------------------SCHEDULE----------------------------------------------------------------
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=abigail&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]

        #Gets the plain text from the dataframe containing the correct season.
        for data in df:
            keys = data.keys()
            if ApiHandler.contains(keys, season):
                text = data[season][0]
        
        returnString = AbigailHandler.parse_currentWeekday(text, weekday.lower())
        return returnString
        return "No such NPC/season. Check your command."

    #Needs to be able to parse out multiple day options like 'Monday, Tuesday, Wednesday and Thursday'
    def parse_currentWeekday(text, weekday):
        splitText = text.split()
        returnString = "Does not include deviations such as single date events or rainy days.\n"
        daySet = set([])

        startIdx = 0

        for idx, word in enumerate(splitText):
            if (word in WEEKDAYS)or (word[0: len(word) -1] in WEEKDAYS):
                daySet = AbigailHandler.parse_dayset(splitText, idx)

            if (weekday in daySet): 
                startIdx = idx
                break

        returnString = AbigailHandler.build_return_schedule(splitText, startIdx)

        print(returnString)
        return returnString

    #parses out the days of the current section
    def parse_dayset(splitText, startidx):
        daySet = set([])

        for word in splitText[startidx: ]:
            if (word == 'and'):
                continue
            elif (word in WEEKDAYS):
                daySet.add(word.lower())
            elif (word[0: len(word) -1] in WEEKDAYS):
                daySet.add(word[ 0 : len(word) - 1].lower())
            else:
                break
        return daySet

    def build_return_schedule(splitText, startIdx):
        first = True
        switchedFromDays = False
        returnString = "*Does not include deviations such as single date events or rainy days.*\n"
        for word in splitText[startIdx:]:

            if (not switchedFromDays):
                if (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) and first:
                    returnString += word
                    first = False
                elif (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) or (word == 'and'):
                    returnString += ' ' + word
                else: 
                    switchedFromDays = True

            else:
                if (word == 'Time' or word == 'Location'):
                    continue
                elif (word in WEEKDAYS) or (word[0:len(word) -1] in WEEKDAYS):
                    break
                else:
                    if word[0].isnumeric() and word[2] == ':' or word[1] == ':':
                        returnString += '\n\t\t-' + word
                    elif word == 'Time' or word == 'Location':
                        None
                    else: 
                        returnString += " " + word
        return returnString
    
#--------------------------------------------------------------------------------------------------------