import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

mytext = soup.find('div',class_='flex flex-col gap-3 wb:mt-1 mt-3 wb:w-full wb:px-5')
all_links = mytext.find_all("a", href=True)

live_links = []                  # list

for tag in all_links:
    href = tag["href"]
    if "/live-cricket-scores/" in href:    
        full_link = "https://www.cricbuzz.com" + href
        live_links.append(full_link)
    
    if len(live_links)>4:
        break  
                                     #for loop exit
print(live_links)

print("-"*100)

tm_name = [] 
for i in live_links:
    r = requests.get(i)
    s = BeautifulSoup(r.text, 'html.parser')
    imptext = s.find('div',class_='flex flex-col gap-3 my-2')
    for data1 in imptext.find_all("span",class_='text-cbTxtPrim dark:text-cbWhite block wb:hidden whitespace-nowrap'):
    
        for data2 in imptext.find_all("span",class_='text-cbTxtSec dark:text-cbTxtSec block wb:hidden whitespace-nowrap'):
            print(data2.text,"Vs",data1.text)

        
    print('_'*10)




