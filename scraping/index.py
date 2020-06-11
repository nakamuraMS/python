import sys
import requests
import re
import logging
from bs4 import BeautifulSoup

# バリデーション処理
def validate(args):
    if len(args) != 3:
        logging.warning('引数の数が足りていません')
        return False
    elif not re.match("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", args[1]):
        logging.warning('URLの形式が不正です')
        return False
    else:
        return True

args = sys.argv
result = validate(args)
if result :
    r = requests.get(args[1])
    soup = BeautifulSoup(r.content, 'html.parser')
    element_count = len(soup.find_all(args[2]))
    print('要素数 : ' + str(element_count))
    print(soup.find_all(args[2]))
else :
    logging.error('処理が正常に実行されませんでした')