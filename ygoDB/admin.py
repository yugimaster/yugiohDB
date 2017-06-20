from django.contrib import admin
from django import forms
from ygoDB.models import CardStatus, CardId, Location, Possession, PendulumStatus, LinkStatus,PackList

# Register your models here.
admin.site.register(CardStatus)
admin.site.register(CardId)
admin.site.register(Location)
admin.site.register(Possession)
admin.site.register(PendulumStatus)
admin.site.register(LinkStatus)
admin.site.register(PackList)
