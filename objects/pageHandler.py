from dotenv import load_dotenv
import json
import requests


class pageHandler:
    def __init__(self ):
        self = self

    async def get_pages_search(searched):
        print(searched)
        request = requests.get("https://stardewvalleywiki.com/mediawiki/api.php?action=query&titles=Blacksmith&format=json").json()
        return json.dumps(request)
