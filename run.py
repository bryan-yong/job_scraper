import requests
from bs4 import BeautifulSoup

def extract(page):
  url = 'https://www.indeed.com/jobs?q=developer&l=Philadelphia,%20PA&vjk=eb36adfdb98c3aeb&start={page}'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup  

def transform(soup):
  divs = soup.find_all('div', class_ = 'job_seen_beacon')
  for item in divs:
    title  = item.find('h2', class_ = 'jobTitle').text
    print(title)

print(transform(extract(2)))