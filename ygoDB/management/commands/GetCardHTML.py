import urllib, re, time, zenhan
import requests
from bs4 import BeautifulSoup

p = re.compile(r"<[^>]*?>")


def getCardHTML(name):
    url = "https://ocg.xpg.jp" + getCardURL(name)
    fp = requests.get(url)
    soup = BeautifulSoup(fp.content, "html.parser")
    fp.close
    time.sleep(1)
    return soup


def getCardURL(name):
    url = "https://ocg.xpg.jp/search/search.fcgi?Name=" + urllib.parse.quote(name.encode('Shift_JIS')) + "&Mode=0"
    try:
        fp = requests.get(url)
        soup = BeautifulSoup(fp.content, "html.parser")
        fp.close
        time.sleep(1)
        texts = soup.find_all("a", href=re.compile("/c/+"))
        for text in texts:
            name_tmp = p.sub("", str(text))
            name_tmp = zenhan.z2h(name_tmp.replace('－', '-'), 3)
            if '【' in name_tmp:
                name_tmp = name_tmp[:name_tmp.index("【")]
            if name == name_tmp:
                url_text = text.get("href")
        return url_text
    except urllib.error.HTTPError:
        time.sleep(1)
        return False
