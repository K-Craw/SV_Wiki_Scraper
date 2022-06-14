
import json as JSON

class JSONParser:
    def page_description(json):
        for section in json['parse']['properties']:
            if section['name'] == 'description':
                return section['*']
        return 'NONE_FOUND'