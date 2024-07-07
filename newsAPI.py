import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


def get_titles(category='health', query='Artificial Intelligence'):
    parameters = {
        'apiKey': NEWS_API_KEY,
        'cathegory': category,
        'q': query
    }
    response = requests.get(BASE_URL, params=parameters)

    response_txt = ""

    if response.status_code == 200:
        data = response.json()
        response_txt += f"Total results: {data['totalResults']}\n\n"
        articles = data['articles']
        for article in articles:
           response_txt += f"Title: {article['title']}\n"
           response_txt += f"Description: {article['description']}\n"
           response_txt += f"URL: {article['url']}\n\n"
    else:
       response_txt += "Failed to retrieve news\n"
       response_txt += f"{response.json()}\n\n"

    print(response_txt)

    return response_txt
