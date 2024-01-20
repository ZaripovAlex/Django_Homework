import datetime

from django.core.management.base import BaseCommand

from hw1_app.models import Items


class Command(BaseCommand):
    help = 'Fill database fake data'
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            items = Items(  title=f'Item{i}',
                            description=f'Lorem ipsum dolor sit amet, consectetur adip',
                            price=i*100+i,
                            quantity=i*10,
                            date_created=datetime.date(2000, 1, 1)
                      )
            self.stdout.write(f'{items} created!')
            items.save()