from django.core.management.base import BaseCommand
from hw1_app.models import Items


class Command(BaseCommand):
   help = "Read items by ID"
   def add_arguments(self, parser):
        parser.add_argument('id')
   def handle(self, *args, **kwargs):
       pk = kwargs.get('id')
       item = Items.objects.filter(pk=pk).first()
       self.stdout.write(f'{item}')