# -*- coding: utf-8 -*-
import re
from ygoDB.management.commands import ChangeNumber
from ygoDB.management.commands import SetStatus

p = re.compile(r"<[^>]*?>")


class Card:
    def __init__(self, card_HTML):
        tmp = card_HTML.find_all("td")
        self.name = SetStatus.setName(str(tmp[0]))
        self.yomi = ChangeNumber.takeNumber(self.name).replace('\n', '')
        self.type = SetStatus.setType(tmp[1].string)
        etc = SetStatus.setEtc(tmp, self.type)
        self.lv = etc[0]
        self.attribute = etc[1]
        self.race = etc[2]
        self.attack = etc[3]
        self.defense = etc[4]
        self.material = etc[5]
        self.effect = etc[6]
        self.pendulum_scale = etc[7]
        self.pendulum_effect = etc[8]
        self.link = etc[9]
        self.link_marker = etc[10]
