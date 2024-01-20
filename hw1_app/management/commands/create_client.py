from django.core.management.base import BaseCommand
from hw1_app.models import Client

class Command(BaseCommand):
    help = 'Create client'
    def add_argument(self, parser):
        parser.add_argument('name')
        parser.add_argument('email')
        parser.add_argument('phone')
        parser.add_argument('address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name'),
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client(
            name=name,
            email=email,
            phone=phone,
            address=address,)
        self.stdout.write(f'Client {client} created')
        client.save()