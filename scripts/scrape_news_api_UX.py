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
        file.write('| Title | Source | Published |\n')
        file.write('| ----- | ------ | --------- |\n')
        for article in articles:
            title = article['title']
            source = article['source']['name']
            published_at = article['publishedAt'].split('T')[0]  # Format the date
            url = article['url']
            file.write(f"| [{title}]({url}) | {source} | {published_at} |\n")
        file.write('\n')

api_key = os.environ.get('NEWS_API_KEY')  # Get API key from environment variable
if not api_key:
    raise Exception("No API key found. Set the NEWS_API_KEY environment variable.")

keywords = ["Pharmaceutical Industry", "Life Sciences", "Medical Devices", "Healthcare Sector", "Pharma Market Trends", "FDA Regulations"]  # Example keywords

for keyword in keywords:
    articles = fetch_news(api_key, keyword)
    generate_markdown(articles, keyword)
