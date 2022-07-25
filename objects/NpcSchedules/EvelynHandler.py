from calendar import week
from turtle import Pen
import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

#Abigail handler parses her schedule correctly.

class EvelynHandler:
#----------------------------------SCHEDULE METHODS----------------------------------------------------------------
    #Calls the API handler to get the schedule and finds the correct season to pass to the weekday parser.
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=evelyn&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        returnString = "*excludes single day unique events, rainy day differences, and other deviations. Returns regular schedule if no specific schedule assigned.*\n"
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]
        if (weekday == 'Monday' or weekday == 'Thursday' or weekday == 'Saturday'):
            for data in df:
                    keys = data.keys()
                    if ApiHandler.contains(keys, 'Monday, Thursday, Saturday (community center repaired)'):
                        timeTxt = data['Monday, Thursday, Saturday (community center repaired)']
                        locationTxt = data['Monday, Thursday, Saturday (community center repaired).1']
                        returnString += EvelynHandler.build_return_schedule(timeTxt, locationTxt, 'Monday, Thursday, Saturday (community center repaired)')

        #Gets the plain text from the dataframe containing the correct season.

        if (season != 'Summer'):
            for data in df:
                keys = data.keys()
                if ApiHandler.contains(keys, 'Normal Daily Schedule'):
                    timeTxt = data['Normal Daily Schedule']
                    locationTxt = data['Normal Daily Schedule.1']
                    returnString += EvelynHandler.build_return_schedule(timeTxt, locationTxt, 'Regular Schedule')
        else:
            for data in df:
                keys = data.keys()
                if ApiHandler.contains(keys, 'Summer Daily Schedule'):
                    timeTxt = data['Summer Daily Schedule']
                    locationTxt = data['Summer Daily Schedule.1']
                    returnString += EvelynHandler.build_return_schedule(timeTxt, locationTxt, 'Summer Regular Schedule')

        return returnString
        return "No such NPC/season. Check your command."
        

    #Builds the string to return once the correct section of the text has been found by parse_dayset and parse_currentWeekday.
    def build_return_schedule(timeTxt, locationTxt, day):
        #switched from days becomes true when the first non-weekday word is found.
        #Then, once another weekday is found, we know we have found the start of another section,
        #and we can break and return.
        returnTxt = ""
        returnTxt = returnTxt + day + "\n"

        for i in range(len(timeTxt)):
            returnTxt += "\t-"
            returnTxt += timeTxt[i]
            returnTxt += " " + locationTxt[i] + "\n"

        return returnTxt
        return returnString
    
#---------------------------------------------------------------------------------------------------