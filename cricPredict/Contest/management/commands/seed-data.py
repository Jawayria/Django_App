from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from Contest.models import League, Match
import json
from random import randint
from datetime import datetime
from datetime import timedelta
from django.utils.timezone import get_current_timezone


class Command(BaseCommand):
    help = 'Enters records for leagues and matches to DB'

    def handle(self, *args, **kwargs):

        for index in range(5):
            start_date = datetime( randint(2021,2022), randint(1, 12),randint(1, 28), tzinfo=get_current_timezone())
            new_league = League(name="League"+str(index), start_date=start_date.strftime("%Y-%m-%d"),
                                end_date=(start_date+timedelta(randint(35, 45))).strftime("%Y-%m-%d"))

            new_league.save()
            league=League.objects.filter(name="League"+str(index))
            teams = []

            for i in range(randint(5,8)):
                teams.append("team"+str(index)+" "+str(i))

            for i in range(randint(15,20)):
                num = randint(0, len(teams)-1)
                t1 = teams[num]
                t2 = teams[(num+1) % len(teams)]
                new_match = Match(team1=t1, team2=t2, time=start_date+timedelta(days=i, hours=randint(7,17)),
                                  league=league[0])
                new_match.save()

        self.stdout.write(self.style.SUCCESS('Successfully added leagues to DB '))
