import pandas as pd
import json as JSON

class JSONParser:
    def page_description(json):
        for section in json['parse']['properties']:
            if section['name'] == 'description':
                return section['*']
        return 'NONE_FOUND'

    def get_queried_members(json):
        return json['query']['categorymembers']
        return 'NONE_FOUND'
    
    def get_parsed_wikitext(json):
        return json['parse']['wikitext']['*']

    def parse_gifts(gifts, desireLevel, npc):
        html = gifts['parse']['text']['*']
        df = pd.read_html(html)

        newString = f'{npc} {desireLevel}:'
        for item in df[1]['Name']:
            newString += f'\n\t- {item}.'
        return newString