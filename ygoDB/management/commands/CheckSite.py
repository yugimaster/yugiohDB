from ygoDB.management.commands import CheckKATAKANA
import jaconv


def checkSite(name, yomi, soup):
    if not (CheckKATAKANA.checkKatakana(name)):
        try:
            soup_yomi = soup.find('h2').span.string
            soup_yomi = soup_yomi.replace('−', '-')
            soup_yomi = soup_yomi.replace('－', '-')
            soup_yomi = jaconv.hira2kata(soup_yomi[soup_yomi.index('(') + 1:soup_yomi.index(')')])
        except ValueError:
            print('サイト側に読みがありません')
            return False
        except AttributeError:
            print('サイト側に読みがありません')
            return False
        yomi = jaconv.hira2kata(yomi)
        if yomi == soup_yomi:
            print('TRUE')
            return True
        else:
            print('FALSE')
            return False
    else:
        return True
