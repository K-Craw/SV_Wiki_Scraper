
import json as JSON

class JSONParser:
    def page_description(json):
        for section in json['parse']['properties']:
            if section['name'] == 'description':
                return section['*']
        return 'NONE_FOUND'


    def get_category_members(json):
        print(json)
        return json['query']['categorymembers']
        return 'NONE_FOUND'