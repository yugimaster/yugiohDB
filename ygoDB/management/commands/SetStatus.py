import zenhan
import re

p = re.compile(r"<[^>]*?>")


def setName(string):
    name = zenhan.z2h(p.sub("", string).replace('－', '-'), 3)
    if '】' in name:
        name = name[:name.index('【')]
    return name


def setType(string,
            types=['L', 'P', 'S', 'X', 'スピリット', 'チューナー', 'デュアル', 'トゥーン', 'ユニオン', 'リバース', '儀式', '効果', '特殊召喚', '融合',
                   '通常']):
    if '特召' in string:
        string = string.replace('特召', '特殊召喚')
    string = zenhan.h2z(string, zenhan.KANA)
    if not ('魔法' in string or '罠' in string):
        for type in types:
            if type in string:
                string = string.replace(type, '/' + type)
        string = string[1:]
    string = zenhan.h2z(string, 4)
    type_array = string.split('/')
    return type_array


def setEtc(tmp, type):
    # etc[lv,属性,種族,atk,def,material,effect,pscale,peffect,link,marker]
    etc = [13, "", "", -2, -2, "", "", -1, "", -1, []]
    if '魔法' in type[0] or '罠' in type[0]:
        etc[6] = setEffect(str(tmp[4]), "")
    else:
        etc[1] = tmp[3].string
        etc[2] = tmp[4].string
        etc[3] = tmp[5].string
        if 'L' in type:
            etc[5] = setMaterial(str(tmp[8]))
            etc[6] = setEffect(str(tmp[8]), etc[5])
            etc[9] = int(tmp[2].string)
            etc[10] = setLinkMarker(tmp)
        else:
            etc[0] = tmp[2].string
            etc[4] = tmp[6].string
            if 'P' in type:
                effect = str(tmp[8]).split("】")
                etc[7] = setPendulumScale(effect[0])
                etc[8] = p.sub("", effect[1][:effect[1].index('【')])
                if '融合' in type or 'S' in type or 'X' in type:
                    effect_tmp = effect[2][effect[2].index("<br/>") + len("<br/>"):]
                    etc[5] = setMaterial(effect_tmp[:effect_tmp.index("<br/>")])
                    etc[6] = setEffect(effect_tmp, etc[5])
                else:
                    etc[6] = setEffect(effect[2], "")
            elif '融合' in type or 'S' in type or 'X' in type:
                etc[5] = setMaterial(str(tmp[8]))
                etc[6] = setEffect(str(tmp[8]), etc[5])
            else:
                etc[6] = setEffect(str(tmp[8]), "")
        if 'このカード' in etc[5]:
            etc[6] = etc[5] + etc[6]
            etc[5] = ''
        if isinstance(etc[3], str):
            etc[3] = int(etc[3].replace('?', '-1'))
        if isinstance(etc[4], str):
            etc[4] = int(etc[4].replace('?', '-1'))
    return etc


def setMaterial(string):
    string = zenhan.z2h(string.replace('－', '-'), 3)
    if '<br' in string:
        string = p.sub("", string[:string.index('<br')])
    else:
        string = p.sub("", string)
    return string


def setEffect(string, material):
    effect = p.sub("", string)
    effect = effect.replace('－', '-')
    effect = zenhan.z2h(effect, 3)
    effect = effect.replace(material, "")
    effect = effect.replace("。", "。\n")
    return effect


def setPendulumScale(scale):
    scale = int(zenhan.z2h(scale[scale.index('赤') + 1:]))
    return scale


def setLinkMarker(origin):
    link_marker = []
    for i in range(9, 18):
        if 'class="s"' in str(origin[i]):
            link_marker.append(i - 9)
    return link_marker
