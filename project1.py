import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores/current_matches"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
all_links = soup.find_all("a", href=True)



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

