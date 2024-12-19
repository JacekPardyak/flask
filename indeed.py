import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?q=Data+Scientist&l=Remote'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
# Your scraping code here...
else:
  print(f"Failed to retrieve page: {response.status_code}")
  
