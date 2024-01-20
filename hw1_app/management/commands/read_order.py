from django.core.management.base import BaseCommand
from hw1_app.models import Order


class Command(BaseCommand):
   help = "Read order by ID"
   def add_arguments(self, parser):
        parser.add_argument('id')
   def handle(self, *args, **kwargs):
       pk = kwargs.get('id')
       order = Order.objects.filter(pk=pk).first()
       self.stdout.write(f'{order}')