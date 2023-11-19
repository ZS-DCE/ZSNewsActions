import os
import requests

def fetch_news(api_key, keyword):
    url = f'https://newsapi.org/v2/everything?q={keyword}&pageSize=25&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    data = response.json()
    return data['articles']

def generate_markdown(articles, keyword):
    with open('README.md', 'a') as file:
        file.write(f'## News for {keyword}\n\n')
        for article in articles:
            title = article['title']
            url = article['url']
            file.write(f"* [{title}]({url})\n")
        file.write('\n')

api_key = os.environ.get('NEWS_API_KEY')  # Get API key from environment variable
if not api_key:
    raise Exception("No API key found. Set the NEWS_API_KEY environment variable.")

keywords = ["ZS Associates", "Another Keyword"]

for keyword in keywords:
    articles = fetch_news(api_key, keyword)
    generate_markdown(articles, keyword)
