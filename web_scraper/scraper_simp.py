from pprint import pprint
import requests
from bs4 import BeautifulSoup


list_a = []

response = requests.get('https://powplanner.com/california/ski-shops')

soup = BeautifulSoup(response.content, 'html.parser')

content_div = soup.find('div').get_attribute_list("h2")

print("starting here")


pprint(content_div)

print("ends here")





