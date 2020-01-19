import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sejuku.net/blog/51241')
soup = BeautifulSoup(r.content, 'html.parser')

element_count = len(soup.find_all('ul'))
print('要素数 : ' + str(element_count))
print(soup.find_all('ul'))