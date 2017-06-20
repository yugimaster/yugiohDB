from ygoDB.models import LinkStatus, CardStatus, PendulumStatus


def upload(card):
    card_status = CardStatus(name=card.name,
                             phonetic=card.yomi,
                             material=card.material,
                             effect=card.effect)
    for i in card.type:
        card_status.type.add(i)
    if card.lv != 13:
        card_status.lv = card.lv
    if card.attribute != 1:
        card_status.attribute = card.attribute
    if card.race != "":
        card_status.race = card.race
    if card.attack != -2:
        card_status.attack = card.attack
    if card.defense != -2:
        card_status.defence = card.defense
    card_status.save()

    if card.pendulum_scale != -1:
        pendulum_status = PendulumStatus(name=CardStatus.objects.get(name=card.name),
                                         pendulum_scale=card.pendulum_scale,
                                         pendulum_effect=card.pendulum_effect)
        pendulum_status.save()

    if card.link != -1:
        link_status = LinkStatus(name=CardStatus.objects.get(name=card.name),
                                 link=card.link,)
        for i in card.link_marker:
            link_status.link_marker.add(i)
        link_status.save()
    return
