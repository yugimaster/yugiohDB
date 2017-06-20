import re

def checkKatakana(str):
    regexp = u'([^ァ-ンヴぁ-んー・\s\-\?!])'
    if re.search(regexp, str) is None:
        return True
    else:
        return False
