from cmath import nan
import math
from numpy import NaN, isin
import pandas as pd


#Used to parse and handle the JSON replies from APIHandler and return the useful information from them.
class JSONParser:

    #Parses the basic description of a page out of it's JSON and returns it as a string.
    def page_description(json):
        for section in json['parse']['properties']:
            if section['name'] == 'description':
                return section['*']
        return 'NONE_FOUND'

    #Parses the members out of a category query and returns them as an array.
    def get_queried_members(json):
        return json['query']['categorymembers']
        return 'NONE_FOUND'
    
    #Parses out wikitext and returns it.
    def get_parsed_wikitext(json):
        return json['parse']['wikitext']['*']

    #Parses gifts out of an an NPC's given gift section
    #into a dataframe
    #and returns a string of the gifts.
    def parse_gifts(gifts, desireLevel, npc):
        html = gifts['parse']['text']['*']
        df = pd.read_html(html)

        newString = f'{npc} {desireLevel}:'
        for item in df[1]['Name']:
            newString += f'\n\t- {item}.'
        return newString

    ##Currently only parsing spring, need to parse any time
    def parse_location_dictionary(df):
        return
        """ locations = []
        times = []

        for time in df[0]['Spring']:
            if (time[0].isnumeric()):
                times.append(time)

        for location in df[0]['Unnamed: 1']:
            #if (location != 'location' and location != 'Location' and isinstance(location, str)):
            if isinstance(location, str):
                #print(location + '\n')
                locations.append(location)

        print(len(locations))
        print('\n')
        print(len(times))
        
        timeLocDict = {}
        for x in range(0, len(times)):
            print(locations[x])
            timeLocDict[times[x]] = locations[x]

        return timeLocDict """