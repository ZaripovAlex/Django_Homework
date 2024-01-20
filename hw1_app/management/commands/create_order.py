from django.core.management.base import BaseCommand
from hw1_app.models import Order, Client, Items

class Command(BaseCommand):
    help = 'Create order'
    def add_argument(self, parser):
        parser.add_argument('client')
        parser.add_argument('items')
        parser.add_argument('total')

    def handle(self, *args, **kwargs):
        client = kwargs.get('client')
        list = kwargs.get('items')
        total = kwargs.get('total')
        client = Client.objects.filter(pk=client).first()
        client = Client(
            name=name,
            email=email,
            phone=phone,
            address=address,)
        self.stdout.write(f'Client {client} created')
        client.save()