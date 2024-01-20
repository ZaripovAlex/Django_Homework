from django.core.management.base import BaseCommand
from hw1_app.models import Client

class Command(BaseCommand):
    help = 'Delete client'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **kwargs):
        id = kwargs.get('id')
        client = Client.objects.filter(pk=id).first()
        self.stdout.write(f'Client {client} deleted')
        client.delete()
        