import requests
import json

def fetch_random_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        # Fix improperly escaped single quotes
        fixed_response = response.text.replace("\\'", "'")
        data = json.loads(fixed_response)
        return data.get("quoteText"), data.get("quoteAuthor")
    except requests.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None, None

quote, author = fetch_random_quote()
if quote:
    print(f'"{quote}" - {author}')
