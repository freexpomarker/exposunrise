import requests
from bs4 import BeautifulSoup
import json

def scrape_and_save():
    url = "freexpomarker.github.io/expo4rat"  # Change to the website you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

   
    paragraphs = soup.find_all('p')
    scraped_data = [p.get_text().strip() for p in paragraphs if p.get_text().strip()]

   
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)


scrape_and_save()
