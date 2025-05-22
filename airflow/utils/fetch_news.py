import requests

def get_top_headlines(api_key, country="us", count=5):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    articles = response.json().get("articles", [])[:count]
    return articles