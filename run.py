import json
import requests
from post import Post
from bs4 import BeautifulSoup

posts = []

def extract(page):
  url = r'https://www.indeed.com/jobs?q=software%20engineer&l=Philadelphia,%20PA&vjk=f5654166e6cd7ff4&start={page}'
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup  

def transform(soup):
  divs = soup.find_all('div', class_ = 'job_seen_beacon')
  for item in divs:
    title  = item.find('h2', class_ = 'jobTitle').text
    if title[0:3] == 'new': title = title[3:]
    company = item.find('span', class_ = 'companyName').text
    location = item.find('div', class_ = 'companyLocation').text
    salary = item.select('.estimated-salary span')
    if len(salary) == 0: salary = 'No Salary Given'
    else: salary = str(salary[0])[6:-7]
    # print('Title: ' + title +'\nCompany: ' + company + '\nLocation: ' + location + '\nSalary: ' + salary + '\n')
    json_obj = {'title':title,
         'company':company,
         'location':location,
         'salary':salary}
    posts.append(json_obj)
    # posts.append(Post(title, company, location, salary))
    
with open('json_file.json', 'w') as file:
    transform(extract(0))
    json.dump(posts, file) 
    
