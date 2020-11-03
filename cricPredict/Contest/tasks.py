from celery.schedules import crontab
from celery.task import task, periodic_task
import requests
import json
from .models import League, Match
from datetime import datetime


@periodic_task(run_every=(crontab(minute='*')), name="fetch_data", ignore_result=True)
def fetch_data():
    url = "https://rapidapi.p.rapidapi.com/series.php"

    headers = {
        'x-rapidapi-key': "94d65a12cbmsh65295dae3718214p1ee3b8jsn335c8c3f26ef",
        'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    response = json.loads(response.text)

    for series in response['seriesList']['series']:

        start_date = series['startDateTime'].split('/')
        start_date = datetime(int(start_date[2]), int(start_date[0]), int(start_date[1]))

        if start_date > datetime.now():

            url = "https://rapidapi.p.rapidapi.com/seriesteams.php"
            teams = requests.get(url, headers=headers, params={"seriesid":series["id"]})
            teams = json.loads(teams.text)

            if len(teams['seriesTeams']['teams']) >= 2:
                end_date = series['endDateTime'].split('/')
                end_date = datetime(int(end_date[2]), int(end_date[0]), int(end_date[1]))

                league = League(name=series['name'], start_date=start_date.strftime("%Y-%m-%d"),
                                end_date=end_date.strftime("%Y-%m-%d"))

                url = "https://rapidapi.p.rapidapi.com/matchseries.php"
                matches = requests.get(url, headers=headers, params={"seriesid":series["id"]})
                matches = json.loads(matches.text)

                # create match objects and save data in DB
    return response['seriesList']


