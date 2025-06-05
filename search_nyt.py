import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def search_articles(search_term):
    params = {
        "q": search_term,
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params)
    return response.json()

def display_results(search_results):
    docs = search_results["response"]["docs"]
    for doc in docs:
        headline = doc["headline"]["main"]
        web_url = doc["web_url"]
        print(f"{headline} ({web_url})")

# while True:
#     search_term = input("Enter search term (or 'exit' to quit): ")
#     search_results = search_articles(search_term)
#     display_results(search_results)
#     print()
    
search_term = "programming"
search_results = search_articles(search_term)
print()
display_results(search_results)
print()