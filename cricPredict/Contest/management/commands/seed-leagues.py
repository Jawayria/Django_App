from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from Contest.models import League
import json


class Command(BaseCommand):
    help = 'Enters records for leagues to DB'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **kwargs):

        script_location = Path(__file__).absolute().parent
        file_location = Path(__file__).absolute().parent/kwargs['file_name']
        file = open(file_location,)
        data = json.load(file)
        for i in data["leagues"]:

            new_record = League(name=i["name"], start_date=i['start-date'], end_date=i['end-date'])
            new_record.save()

        self.stdout.write(self.style.SUCCESS('Successfully added leagues to DB '))
