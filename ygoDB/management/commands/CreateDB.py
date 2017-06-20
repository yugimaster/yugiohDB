from ygoDB.management.commands import Card
from ygoDB.management.commands import UploadStatus
from ygoDB.management.commands import UploadId
from ygoDB.management.commands import GetHTML,GetCardHTML
import gc
from ygoDB.management.commands import CheckSite
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        start()


def start():
    GetHTML.getHTML()
    f = open('text/text.txt', 'r', encoding='utf-8')
    data1 = f.read()
    f.close()
    del f
    gc.collect()

    print("元ファイル読み込み完了")
    data = data1.split("\n")
    del data1
    gc.collect()

    white_list = open('text/white.txt', 'r', encoding='utf-8')
    check_list = white_list.read()
    print("check_list作成完了")
    white_list.close()

    exception = open('text/exception.txt', 'r', encoding='utf-8')
    exception_list = exception.read()
    print("exception_list作成完了")
    exception.close()

    for line in data:
        soup = BeautifulSoup(line, "html.parser")
        card_HTMLs = soup.find_all("tbody")
        for card_HTML in card_HTMLs:
            card = Card.Card(card_HTML)
            print(card.name)
            if not (card.name + '\n' in check_list):
                soup = GetCardHTML.getCardHTML(card.name)
                if CheckSite.checkSite(card.name,card.yomi,soup) or card.name + ',' in exception_list:
                    UploadStatus.upload(card)
                    UploadId.uploadId(card.name,soup)
                    white_list = open('text/white.txt', 'a+', encoding='utf-8')
                    white_list.write(card.name + '\n')
                    check_list = check_list + card.name + '\n'
                    white_list.close()
                else:
                    print(card.yomi + ':読みが違います')
                    exception = open('text/error.txt', 'a', encoding='utf-8')
                    exception.write(card.name + ',' + card.yomi + '\n')
                    exception.close()
            else:
                print("書き込み済み")
