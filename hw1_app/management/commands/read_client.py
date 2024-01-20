from django.core.management.base import BaseCommand
from hw1_app.models import Client


class Command(BaseCommand):
   help = "Read client"
   def add_arguments(self, parser):
        parser.add_argument('id')
   def handle(self, *args, **kwargs):
       pk = kwargs.get('id')
       client = Client.objects.filter(pk=pk).first()
       self.stdout.write(f'{client}')