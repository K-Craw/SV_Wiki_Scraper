from calendar import week
from turtle import Pen
import requests
import pandas as pd
from objects.ApiHandler import ApiHandler

ENDPOINT ='https://stardewvalleywiki.com/mediawiki/api.php?'

SEASONS = set(['spring', 'summer', 'fall', 'winter'])

WEEKDAYS = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

#Abigail handler parses her schedule correctly.

class GusHandler:
#----------------------------------SCHEDULE METHODS----------------------------------------------------------------
    #Calls the API handler to get the schedule and finds the correct season to pass to the weekday parser.
    async def get_schedule(season, weekday):
        requested_JSON = requests.get(f"{ENDPOINT}action=parse&section=1&page=gus&format=json").json()
        html = requested_JSON['parse']['text']['*']
        df = pd.read_html(html)
        returnString = "*excludes single day unique events, rainy day differences, and other deviations. Returns regular schedule if no specific schedule assigned.*\n"
        #turns the season into an uppercase season for indexing.
        season = season.lower()
        season = season[0].upper() + season[1:len(season)]

        #Gets the plain text from the dataframe containing the correct season.
        found = False

        #searches for the correct season in the data.
        for data in df:
            keys = data.keys()
            if ApiHandler.contains(keys, season):
                timeTxt = data[season]
                locationTxt = data[season + ".1"]
                found = True
                returnString = GusHandler.build_return_schedule(timeTxt, locationTxt, weekday)
            elif ApiHandler.contains(keys, weekday):
                timeTxt = data[weekday]
                locationTxt = data[weekday + ".1"]
                found = True
                returnString = GusHandler.build_return_schedule(timeTxt, locationTxt, weekday)

        #if the season is not found, then instead searches for regular schedule.
        if (not found):
            if (weekday == 'Tuesday'):
                for data in df:
                    keys = data.keys()
                    if ApiHandler.contains(keys, 'Tuesday, community center repaired'):
                        timeTxt = data['Tuesday, community center repaired']
                        locationTxt = data['Tuesday, community center repaired.1']
                        returnString += GusHandler.build_return_schedule(timeTxt, locationTxt, 'Tuesday, community center repaired')
            for data in df:
                keys = data.keys()
                if ApiHandler.contains(keys, 'Normal Schedule'):
                    timeTxt = data['Normal Schedule']
                    locationTxt = data['Normal Schedule.1']
                    returnString += GusHandler.build_return_schedule(timeTxt, locationTxt, 'Regular Schedule')

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