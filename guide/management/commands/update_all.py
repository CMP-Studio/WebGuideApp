from django.core.management.base import BaseCommand, CommandError
from guide.services.update_data import update_data_CMS
from guide.services.update_hours import update_hours_CMS

class Command(BaseCommand):

        def handle(self, *args, **options):
                update_data_CMS()
                update_hours_CMS()
