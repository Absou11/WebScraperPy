import os
import requests
from bs4 import BeautifulSoup

# Prompt the user for a URL
url = input("Enter the URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.pdf') or href.endswith('.jpg') or href.endswith('.png'):
        file_url = url + href if not href.startswith('http') else href
        file_name = os.path.basename(file_url)
        with open(file_name, 'wb') as file:
            response = requests.get(file_url)
            file.write(response.content)

for tag in soup.find_all():
    tag_name = tag.name
    if tag_name == 'a':
        print(tag.get('href'))
    elif tag_name == 'img':
        print(tag.get('src'))
    elif tag_name == 'link':
        print(tag.get('href'))
    elif tag_name == 'script':
        print(tag.get('src'))
