livescore = 'https://www.cricbuzz.com/cricket-match/live-scores'
# from package-name import module name
from bs4 import BeautifulSoup
import requests

req = requests.get(livescore)
soup = BeautifulSoup(req.text, 'html.parser')
imptext = soup.find('div',class_='flex flex-col gap-3 my-2  ')
for data in imptext.find_all("span",class_= "text-cbTxtSec"):
    print(data.text)
print('_'*100)