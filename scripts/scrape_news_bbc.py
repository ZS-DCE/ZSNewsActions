import os
import requests
from bs4 import BeautifulSoup

def scrape_bbc_news(keyword):
    # BBC News doesn't directly support keyword search in URL, so we use a general URL
    url = 'https://www.bbc.co.uk/news'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = []

    for item in soup.find_all('div', class_='gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'):
        title_element = item.find('h3')
        if title_element:
            title = title_element.text.strip()
            link = 'https://www.bbc.co.uk' + item.find('a', href=True)['href']

            # Simple keyword matching
            if keyword.lower() in title.lower():
                news_items.append((title, link))
                if len(news_items) == 25:
                    break

    return news_items

def generate_markdown(articles, keyword, file):
    file.write(f'## News for {keyword}\n\n')
    file.write('| Title | Link |\n')
    file.write('| ----- | ---- |\n')
    for title, link in articles:
        file.write(f"| [{title}]({link}) |\n")
    file.write('\n')

# Open the README.md file in write mode to refresh its content
with open('README.md', 'w') as file:
    file.write('# Latest News\n\n')
    keywords = ["Pharmaceutical", "Biotechnology"]  # Example keywords
    for keyword in keywords:
        articles = scrape_bbc_news(keyword)
        generate_markdown(articles, keyword, file)
