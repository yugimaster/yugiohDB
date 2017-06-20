from django.db import models

TYPE_SET = (
    ('通常', '通常'),
    ('効果', '効果'),
    ('特殊召喚', '特殊召喚'),
    ('リバース', 'リバース'),
    ('ユニオン', 'ユニオン'),
    ('スピリット', 'スピリット'),
    ('トゥーン', 'トゥーン'),
    ('デュアル', 'デュアル'),
    ('儀式', '儀式'),
    ('P', 'P'),
    ('融合', '融合'),
    ('S', 'S'),
    ('X', 'X'),
    ('L', 'L'),
    ('通常魔法', '通常魔法'),
    ('装備魔法', '装備魔法'),
    ('永続魔法', '永続魔法'),
    ('速攻魔法', '速攻魔法'),
    ('儀式魔法', '儀式魔法'),
    ('フィールド魔法', 'フィールド魔法'),
    ('通常罠', '通常罠'),
    ('永続罠', '永続罠'),
    ('カウンター罠', 'カウンター罠'),
)

ATTRIBUTE_LIST = (
    ('闇', '闇'),
    ('光', '光'),
    ('水', '水'),
    ('炎', '炎'),
    ('地', '地'),
    ('風', '風'),
    ('神', '神'),
)

RACE_LIST = (
    ('ドラゴン', 'ドラゴン族'),
    ('魔法使い', '魔法使い族'),
    ('アンデット', 'アンデット族'),
    ('戦士', '戦士族'),
    ('獣戦士', '獣戦士族'),
    ('獣', '獣族'),
    ('鳥獣', '鳥獣族'),
    ('悪魔', '悪魔族'),
    ('天使', '天使族'),
    ('昆虫', '昆虫族'),
    ('恐竜', '恐竜族'),
    ('爬虫類', '爬虫類族'),
    ('魚', '魚族'),
    ('海竜', '海竜族'),
    ('機械', '機械族'),
    ('雷', '雷族'),
    ('水', '水族'),
    ('炎', '炎族'),
    ('岩石', '岩石族'),
    ('植物', '植物族'),
    ('サイキック', 'サイキック族'),
    ('幻竜', '幻竜族'),
    ('サイバース', 'サイバース族'),
    ('幻神獣', '幻神獣族'),
    ('創造神', '創造神族'),
)

LV_LIST = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13)
)

MARKER_LIST = [
    (0, '左上'),
    (1, '上'),
    (2, '右上'),
    (3, '左'),
    (4, '中央'),
    (5, '右'),
    (6, '左下'),
    (7, '下'),
    (8, '右下')
]


class PackList(models.Model):
    pack_id = models.CharField('pack_id', primary_key=True, max_length=30)
    pack_name = models.CharField('pack_name', unique=True, max_length=255)

    class Meta:
        db_table = 'pack_list'

    def __str__(self):
        return self.pack_name


class CardId(models.Model):
    card_id = models.CharField('card_id', primary_key=True, max_length=30)
    name = models.ForeignKey('CardStatus', related_name='id')
    recording_pack = models.ForeignKey('PackList',related_name='id',default='')

    def __str__(self):
        return self.card_id

    class Meta:
        db_table = 'card_id'


class CardStatus(models.Model):
    name = models.CharField('name', primary_key=True, max_length=255)
    phonetic = models.CharField('phonetic', max_length=255)
    type = models.ManyToManyField('TypeList', related_name='status')
    lv = models.IntegerField('lv', null=True, blank=True, choices=LV_LIST)
    attribute = models.CharField('attribute', max_length=5, null=True, blank=True, choices=ATTRIBUTE_LIST)
    race = models.CharField('race', max_length=10, null=True, blank=True, choices=RACE_LIST)
    attack = models.IntegerField('atk', null=True, blank=True)
    defence = models.IntegerField('def', null=True, blank=True)
    material = models.CharField('material', null=True, blank=True, max_length=100)
    effect = models.TextField('effect', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'card_status'


class TypeList(models.Model):
    type = models.CharField('type', max_length=40, choices=TYPE_SET, primary_key=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'type_list'


class PendulumStatus(models.Model):
    name = models.OneToOneField(CardStatus, primary_key=True, related_name='Pendulum')
    pendulum_scale = models.IntegerField('pendulum_scale', choices=LV_LIST)
    pendulum_effect = models.TextField('pendulum_effect', null=True, blank=True)

    def __str__(self):
        return getattr(self.name, 'name', None)

    class Meta:
        db_table = 'pendulum_status'


class LinkStatus(models.Model):
    name = models.OneToOneField(CardStatus, primary_key=True, related_name='Link')
    link = models.IntegerField('link')
    link_marker = models.ManyToManyField('LinkMarker', related_name='Link')

    def __str__(self):
        return getattr(self.name, 'name', None)

    class Meta:
        db_table = 'link_status'


class LinkMarker(models.Model):
    marker = models.IntegerField('marker', primary_key=True, choices=MARKER_LIST)

    def __str__(self):
        return str(MARKER_LIST[self.marker][1])

    class Meta:
        db_table = 'link_marker'


class Location(models.Model):
    location_name = models.CharField('location_name', max_length=255)

    def __str__(self):
        return self.location_name

    class Meta:
        db_table = 'Location_list'


class Possession(models.Model):
    card_name = models.ForeignKey(CardId, related_name='possession')
    number = models.IntegerField('number')
    location = models.ForeignKey(Location, related_name='location')

    def __str__(self):
        return self.card_name_id

    class Meta:
        db_table = 'possession'
