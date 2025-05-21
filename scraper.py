import requests
from bs4 import BeautifulSoup
import json

def scrape_and_save():
    url = "https://example.com"  # Change to the website you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all paragraph text
    paragraphs = soup.find_all('p')
    scraped_data = [p.get_text().strip() for p in paragraphs if p.get_text().strip()]

    # Save the data permanently to a JSON file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(scraped_data, f, ensure_ascii=False, indent=4)

# Run the function
scrape_and_save()
