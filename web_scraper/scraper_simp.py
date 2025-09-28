import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
