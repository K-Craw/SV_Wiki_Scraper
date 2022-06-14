import requests


class wikiNavHandler:

    async def _get_shops():
        request_url = f"https://stardewvalleywiki.com/mediawiki/api.php?action=query&list=categorymembers&cmtitle=Category:Shops"
        requested_JSON = requests.get(request_url).json()