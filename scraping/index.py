import argparse
import requests
from bs4 import BeautifulSoup

args = sys.argv
r = requests.get(args[1])
soup = BeautifulSoup(r.content, 'html.parser')

element_count = len(soup.find_all(args[2]))
print('要素数 : ' + str(element_count))
print(soup.find_all(args[2]))