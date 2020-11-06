from celery.schedules import crontab
from celery.task import task, periodic_task
import requests
import json
from .models import League, Match
from datetime import datetime
from django.utils.timezone import get_current_timezone
import os
from pathlib import Path
from cricPredict.settings import API_KEY


@periodic_task(run_every=(crontab(minute='*')), name="fetch_data", ignore_result=True)
def fetch_data():
    try:
        url = "https://rapidapi.p.rapidapi.com/series.php"

        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        response = json.loads(response.text)

        league_ids = League.objects.all().values('league_id')

        for series in response['seriesList']['series']:

            if series['id'] not in league_ids:

                start_date = series['startDateTime'].split('/')
                start_date = datetime(int(start_date[2]), int(start_date[0]), int(start_date[1]))

                if start_date > datetime.now():

                    url = "https://rapidapi.p.rapidapi.com/seriesteams.php"
                    teams = requests.get(url, headers=headers, params={"seriesid":series["id"]})
                    teams = json.loads(teams.text)

                    if len(teams['seriesTeams']['teams']) > 2:
                        end_date = series['endDateTime'].split('/')
                        end_date = datetime(int(end_date[2]), int(end_date[0]), int(end_date[1]))

                        league = League(league_id=series['id'], name=series['name'], start_date=start_date.strftime("%Y-%m-%d"),
                                        end_date=end_date.strftime("%Y-%m-%d"))

                        league.save()
                        league = League.objects.filter(league_id=series['id'])[0]

                        url = "https://rapidapi.p.rapidapi.com/matchseries.php"
                        matches = requests.get(url, headers=headers, params={"seriesid":series["id"]})
                        matches = json.loads(matches.text)

                        for match in matches['matchList']['matches']:
                            team1 = match['homeTeam']['name']
                            team2 = match['awayTeam']['name']
                            start_time = datetime.strptime(match['startDateTime'], "%Y-%m-%dT%H:%M:%SZ")\
                                .replace(tzinfo=get_current_timezone())
                            new_match = Match(league=league, team1=team1, team2=team2, time=start_time);
                            new_match.save()

        return True
    except:
        return False

