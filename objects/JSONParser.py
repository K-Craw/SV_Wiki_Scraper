
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

    def get_parsed_loves(wikitext):
        tokens = wikitext.split(" ")
        for token in tokens:
            print(token + " END ")