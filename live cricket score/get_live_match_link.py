import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
all_links = soup.find_all("a", href=True)



live_links = []                  # list



for tag in all_links:
    href = tag["href"]
    if "/live-cricket-scores/" in href:                
        full_link = "https://www.cricbuzz.com" + href
        
        if full_link not in live_links:     # avoid duplicates
            live_links.append(full_link)
    
    if len(live_links) == 5:                # stop after 5 links
        break

print("LIST OF FIRST 5 LIVE MATCH LINKS:\n")
print(live_links)
