

class JSONParser:
    def summary(json):
        for section in json['parse']['properties']:
            if section['name'] == 'description':
                return section['*'] 