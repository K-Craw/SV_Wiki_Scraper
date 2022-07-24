from turtle import Pen
import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

#Abigail handler parses her schedule correctly.

class ElliottHandler:
#----------------------------------SCHEDULE METHODS----------------------------------------------------------------
    #Calls the API handler to get the schedule and finds the correct season to pass to the weekday parser.
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=elliott&format=json").json()
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
        
        returnString = ElliottHandler.parse_currentWeekday(text, weekday.lower())
        return returnString
        return "No such NPC/season. Check your command."

    #Needs to be able to parse out multiple day options like 'Monday, Tuesday, Wednesday and Thursday'
    def parse_currentWeekday(text, weekday):
        splitText = text.split()
        daySet = set([])
        startIdx = 0
        returnString  = "" 

        #checks if each section contains the current weekday by calling parse_dayset each time it finds a set.
        #gets the index of the start and passes it to the return handler to build the output.
        for idx, word in enumerate(splitText):
            #if the word is a day or is a day ending in a comma.
            if (word in WEEKDAYS)or (word[0: len(word) -1] in WEEKDAYS):
                daySet = ElliottHandler.parse_dayset(splitText, idx)
            #if the set now contains the weeekday we're looking for break out
            #and set found to true;
            if (weekday in daySet and weekday != 'tuesday'): 
                startIdx = idx
                returnString += ElliottHandler.build_return_schedule(splitText, startIdx)
                break
        
        #if the requested weekday wasn't found, get the normal schedule.
        for idx, word in enumerate(splitText):
            if (word == 'Regular'):
                daySet = ElliottHandler.parse_dayset(splitText, idx)

            if ('Regular Schedule' in daySet): 
                startIdx = idx
                break

        returnString += '\n'
        returnString += ElliottHandler.build_return_schedule(splitText, startIdx)
        return returnString

    #parses out the days of the current section
    def parse_dayset(splitText, startidx):
        daySet = set([])

        #gets all the weekdays in the current section.
        for word in splitText[startidx: ]:
            if (word == 'and'):
                continue
            elif (word in WEEKDAYS):
                daySet.add(word.lower())
            elif (word[0: len(word) -1] in WEEKDAYS):
                daySet.add(word[ 0 : len(word) - 1].lower())
            elif (word == 'Regular'):
                daySet.add('Regular Schedule')
            else:
                break

        return daySet

    #Builds the string to return once the correct section of the text has been found by parse_dayset and parse_currentWeekday.
    def build_return_schedule(splitText, startIdx):
        #switched from days becomes true when the first non-weekday word is found.
        #Then, once another weekday is found, we know we have found the start of another section,
        #and we can break and return.
        first = True
        switchedFromDays = False
        returnString = "*Does not include deviations such as single date events or rainy days.*\n"

        for word in splitText[startIdx:]:
            #if we're parsing out the weekdays and havent found a non-week word.
            if (not switchedFromDays):
                if (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) and first:
                    returnString += word
                    first = False
                elif (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) or (word == 'and'):
                    returnString += ' ' + word
                else: 
                    if (word != 'Time' and word != 'Location'):
                        returnString += ' ' + word 
                    switchedFromDays = True

            #if we have found a word thats not a weekday or and, perform normal parsing.
            else:
                if (word == 'Time' or word == 'Location'):
                    continue
                elif (word in WEEKDAYS) or (word[0:len(word) -1] in WEEKDAYS) or (word == "Rainy") or (word == "Regular"):
                    break
                else:
                    #if the word is a time create a new time line.
                    if word[0].isnumeric() and (len(word) > 1) and word[1] == ':' or (len(word) > 2) and (word[2] == ':'):
                            returnString += '\n\t\t-' + word
                    elif (word[0].isnumeric()):
                        returnString += ' ' + word
                    elif word == 'Time' or word == 'Location':
                        None
                    else: 
                        returnString += " " + word
        return returnString
    