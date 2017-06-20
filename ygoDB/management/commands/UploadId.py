from ygoDB.models import CardId, CardStatus, PackList


def uploadId(name,soup):
    try:
        table = soup.find("table", class_="Hover w4")
        data = table.find_all("td")
        for i in range(1, len(data), 3):
            id = data[i].string
            card_id = CardId(card_id=id,
                             name=CardStatus.objects.get(name=name),
                             recording_pack=PackList.objects.get(pack_id=id[:id.index('-')]))
            card_id.save()
    except TypeError:
        print(name)