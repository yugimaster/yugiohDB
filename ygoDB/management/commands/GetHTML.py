import urllib.request, urllib.error
import time

from bs4 import BeautifulSoup
from ygoDB.models import PackList

def getHTML():
    fp = urllib.request.urlopen('https://ocg.xpg.jp/v/list/')
    soup = BeautifulSoup(fp, "html.parser")

    white_list = open('text/white_pack.txt', 'r', encoding='utf-8')
    check_list = white_list.read()
    white_list.close()
    if check_list is '':
        f = open('text/text.txt', 'w', encoding='utf-8')
        f.close()
    print("check_list作成完了")
    texts = soup.find_all('tr')
    for text in texts:
        if ('td' in str(text)):
            td_list = text.find_all('td')
            url = 'https://ocg.xpg.jp' + td_list[0].a.get("href")
            if not (url + '\n' in check_list):
                pack_list = PackList(td_list[1].string, td_list[0].string)
                pack_list.save()
                getPackHtml(url)
                check_list = check_list + url + '\n'
                time.sleep(1)
            else:
                print('読み込み済み')


def getPackHtml(url):
    fp = urllib.request.urlopen(url)
    try:
        html = fp.read().decode('Shift_JIS')
        f = open('text/text.txt', 'a', encoding='utf-8')
        f.write(html + '\n')
        fp.close()
    except UnicodeDecodeError:
        url = 'error = ' + url
    print(url)
    white_list = open('text/white_pack.txt', 'a+', encoding='utf-8')
    white_list.write(url + '\n')
    white_list.close()

