#need to check for the target in the first part of his schedule section, and then in the second part
#returning both of them.
from calendar import week
from turtle import Pen
import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

FIRST_TABLE_SIZE = 4;

#Abigail handler parses her schedule correctly.

class LeoHandler:
#----------------------------------SCHEDULE METHODS----------------------------------------------------------------
    #Calls the API handler to get the schedule and finds the correct season to pass to the weekday parser.
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=Leo&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]

        #Gets the plain text from the dataframe containing the correct season.
        found = False
        text = ""

        #searches for the correct weekday in the data.
        returnString = "If you have less than 6 hearts with Leo, he resides at Ginger Island. \n"
        for data in df:
            keys = data.keys()
            if (LeoHandler.contains(keys[0], weekday) and not LeoHandler.contains(keys[0], "the")):
                timeTxt = data[keys[0]]
                locationTxt = data[keys[1]]
                found = True
                returnString += LeoHandler.build_return_schedule_under6(timeTxt, locationTxt, keys[0])
                break
            

        #if the weekday is not found, then instead searches for regular schedule.
        if (not found):
            for data in df:
                keys = data.keys()
                if ApiHandler.contains(keys, 'Regular Schedule'):
                    timeTxt = data['Regular Schedule']
                    locationTxt = data['Regular Schedule.1']
                    returnString += LeoHandler.build_return_schedule_under6(timeTxt, locationTxt, 'Regular Schedule')
                    break

        returnString += "\nIf you have more than 6 hearts with Leo, he resides on The Mountain. \n"

        #need to iterate the second portion of the data, getting the season
        for data in df:
            keys = data.keys()
            if ApiHandler.contains(keys, season):
                text = data[season][0]

        returnString += LeoHandler.parse_currentWeekday(text, weekday.lower())
        return returnString
        return "No such NPC/season. Check your command."
        

    #Builds the string to return once the correct section of the text has been found by parse_dayset and parse_currentWeekday.
    def build_return_schedule_under6(timeTxt, locationTxt, day):
        #switched from days becomes true when the first non-weekday word is found.
        #Then, once another weekday is found, we know we have found the start of another section,
        #and we can break and return.
        returnTxt = "*excludes single day unique events, rainy day differences, and other deviations. Returns regular schedule if no specific schedule assigned.*\n"
        returnTxt = returnTxt + day + "\n"

        for i in range(len(timeTxt)):
            returnTxt += "\t-"
            returnTxt += timeTxt[i]
            returnTxt += " " + locationTxt[i] + "\n"

        return returnTxt
        return returnString


    def build_return_schedule_over6(splitText, startIdx):
        #switched from days becomes true when the first non-weekday word is found.
        #Then, once another weekday is found, we know we have found the start of another section,
        #and we can break and return.
        first = True
        switchedFromDays = False
        returnString = ""

        for word in splitText[startIdx:]:
            #if we're parsing out the weekdays and havent found a non-week word.
            if (not switchedFromDays):
                if (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) and first:
                    returnString += word
                    first = False
                elif (word[0:len(word)-1] in WEEKDAYS) or (word in WEEKDAYS) or (word == 'and'):
                    returnString += ' ' + word
                else: 
                    switchedFromDays = True

            #if we have found a word thats not a weekday or and, perform normal parsing.
            else:
                if (word == 'Time' or word == 'Location'):
                    continue
                elif (word in WEEKDAYS) or (word[0:len(word) -1] in WEEKDAYS):
                    break
                else:
                    #if the word is a time create a new time line.
                    if word[0].isnumeric():
                        if (len(word) > 1) and word[1] == ':': 
                            returnString += '\n\t\t-' + word
                        elif (len(word) > 2) and (word[2] == ':'):
                            returnString += '\n\t\t-' + word
                    elif word == 'Time' or word == 'Location':
                        None
                    else: 
                        returnString += " " + word
        return returnString
    
    def parse_currentWeekday(text, weekday):
        splitText = text.split()
        daySet = set([])
        startIdx = 0

        #checks if each section contains the current weekday by calling parse_dayset each time it finds a set.
        #gets the index of the start and passes it to the return handler to build the output.
        for idx, word in enumerate(splitText):
            if (word in WEEKDAYS)or (word[0: len(word) -1] in WEEKDAYS):
                daySet = LeoHandler.parse_dayset(splitText, idx)

            if (weekday in daySet): 
                startIdx = idx
                break

        return LeoHandler.build_return_schedule_over6(splitText, startIdx)
#---------------------------------------------------------------------------------------------------

    def contains(text, wordToFind):
        text = text.split(" ")
        foundWord = False
        for word in text:
            if word == wordToFind or word[0:len(word) - 1] == wordToFind:
                foundWord = True
            if (foundWord and word.isnumeric()):
                return False
        return foundWord

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
            elif (word == 'Normal'):
                daySet.add('Normal Schedule')
            else:
                break

        return daySet