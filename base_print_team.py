livescore = 'https://www.cricbuzz.com/cricket-match/live-scores'

from bs4 import BeautifulSoup
import requests

req = requests.get(livescore)
soup = BeautifulSoup(req.text, 'html.parser')
imptext = soup.find('div',class_='flex flex-col gap-3 my-2')

for data1 in imptext.find_all("span",class_='text-cbTxtPrim dark:text-cbWhite block wb:hidden whitespace-nowrap'):   
    for data2 in imptext.find_all("span",class_='text-cbTxtSec dark:text-cbTxtSec block wb:hidden whitespace-nowrap'):
        print(data2.text,"Vs",data1.text)
    
print('_'*10)