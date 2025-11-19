livescore = 'https://www.cricbuzz.com/live-cricket-scores/124629/tn-vs-up-elite-group-a-ranji-trophy-elite-2025-26'
# from package-name import module name
from bs4 import BeautifulSoup
import requests

req = requests.get(livescore)
soup = BeautifulSoup(req.text, 'html.parser')
imptext = soup.find('a',class_='w-full bg-cbWhite flex flex-col p-3 gap-1')
for data in imptext.find_all('span'):
    print(data.text)
print('_'*100)
    
   