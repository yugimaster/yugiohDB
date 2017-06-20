from django.core.management.base import BaseCommand
from ygoDB.models import LinkStatus, CardStatus, PendulumStatus



class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hello')
        CardStatus.objects.all().delete()
        white_list = open('text/white.txt', 'w', encoding='utf-8')
        white_list.close()

