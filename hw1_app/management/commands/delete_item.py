from django.core.management.base import BaseCommand
from hw1_app.models import Items


class Command(BaseCommand):
    help = "Delete product by id"
    def add_arguments(self, parser):
        parser.add_argument('id', type=int)
    def handle(self, *args, **kwargs):
        pk = kwargs.get('id')
        item = Items.objects.filter(pk=pk).first()
        self.stdout.write(f'{item} deleted')
        item.delete()