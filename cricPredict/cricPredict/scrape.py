from bs4 import BeautifulSoup
import urllib.request
score_page = 'https://www.espncricinfo.com/ci/content/match/fixtures_futures.html'
while True:
 page = urllib.request.urlopen(score_page)
 soup = BeautifulSoup(page, 'html.parser')
 result = soup.find('div', {'id':'second'})
 print(result)
 message = input('Do you want to refresh scores? [Y/N]')
 if message == 'Y':
     print('------------------------------------------')
     for match in result:
         print(match.find_all('li')).get_text()
 elif message == 'N':
     break
 else:
     print('Please enter "Y" or "N" only.')
     continue