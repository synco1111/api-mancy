# TODO
# https://www.sefaria.org.il/texts/Tanakh
# https://github.com/Sefaria
# http://m.ibibles.net/quote05.htm
# https://api.scripture.api.bible
# https://github.com/Sefaria/Sefaria-Project/wiki/API-Documentation#index-api <------ Choose this one
import requests
from pprint import pprint

# bible_variables
    scripture_api_bible_token = 'fff1527292a4eaa5cfb9c5a099b9782f' # export to env variable
new_testament_bible_hebrew = 'a8a97eebae3c98e4-01'
king_james_english = 'de4e12af7f28f599-01'



def get_bible_by_id(new_testament_bible_hebrew):
    url = 
    payload={}
    headers = {
    'accept': 'application/json',
    'api-key': scripture_api_bible_token
    }
    return requests.request("GET", url, headers=headers, data=payload).json()
    # hebrew_bible_id = response['data'][0]['id']

