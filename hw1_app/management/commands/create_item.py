from django.core.management.base import BaseCommand
from hw1_app.models import Items

class Command(BaseCommand):
    help = 'Create item'
    def add_argument(self, parser):
        parser.add_argument('title')
        parser.add_argument('description')
        parser.add_argument('price')
        parser.add_argument('quantity')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs('price')
        quantity = kwargs('quantity')
        item = Items(
            title=title,
            description=description,
            price=price,
            quantity=quantity,)
        self.stdout.write(f'Item {item} created')
        item.save()
        
