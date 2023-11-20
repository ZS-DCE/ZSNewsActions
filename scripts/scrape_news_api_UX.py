import os
import requests

def fetch_news(api_key, keyword):
    url = f'https://newsapi.org/v2/everything?q={keyword}&pageSize=25&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching news: {response.status_code}")
    data = response.json()
    return data['articles']

def generate_markdown(articles, keyword, file):
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

# Open the README.md file in write mode to refresh its content
with open('README.md', 'w') as file:
    file.write('# Latest News\n\n')
    keywords = ["Pharmaceutical Industry",
"New Drug Approvals",
"FDA Approval",
"Clinical Trials",
"Drug Development",
"Pharma Mergers & Acquisitions",
"Pharmaceutical Regulation",
"Drug Safety",
"Pharma Patent",
"Life Sciences",
"Biotechnology",
"Genomics",
"CRISPR",
"Bioinformatics",
"Molecular Biology",
"Cell Therapy",
"Precision Medicine",
"Life Science Research",
"Medical Devices",
"Medical Device Innovation",
"FDA Device Approval",
"Wearable Health Tech",
"Medical Imaging Technology",
"Surgical Instruments",
"Diagnostic Equipment",
"Healthcare Sector",
"Digital Health",
"Telemedicine",
"Healthcare Policy",
"Patient Care Innovation",
"Health Insurance",
"Public Health",
"Specific Therapeutic Areas",
"Oncology",
"Neurology",
"Cardiology",
"Immunology",
"Diabetes",
"Rare Diseases",
"Business and Market Trends",
"Pharma Market Trends",
"Biotech Startups",
"Healthcare Investment",
"Biopharma Partnerships",
"Pharmaceutical Marketing",
"Emerging Technologies",
"AI in Pharma",
"Machine Learning in Drug Discovery",
"Blockchain in Healthcare",
"3D Printing in Medicine",
"Regulatory and Compliance",
"FDA Regulations",
"EMA Guidelines",
"Clinical Trial Regulation",
"Healthcare Compliance"]  # Example keywords

    for keyword in keywords:
        articles = fetch_news(api_key, keyword)
        generate_markdown(articles, keyword, file)
