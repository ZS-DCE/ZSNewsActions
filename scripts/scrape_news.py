import requests
from bs4 import BeautifulSoup

def scrape_google_news(keyword):
    url = f"https://www.google.com/search?q={keyword}&tbm=nws"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.find_all('div', class_='dbsr'):
        title = item.find('div', class_='JheGif nDgy9d').get_text()
        link = item.a['href']
        news_items.append((title, link))
        if len(news_items) == 25:
            break

    return news_items

def generate_markdown(news_items, keyword):
    with open('README.md', 'a') as file:
        file.write(f'## News for {keyword}\n\n')
        for title, link in news_items:
            file.write(f"* [{title}]({link})\n")
        file.write('\n')

keywords = ["ZS Associates", "Pharma"]
for keyword in keywords:
    news_items = scrape_google_news(keyword)
    generate_markdown(news_items, keyword)
