'''
livescore = 'https://www.cricbuzz.com/cricket-match/live-scores'
# from package-name import module name
from bs4 import BeautifulSoup
import requests

req = requests.get(livescore)
soup = BeautifulSoup(req.text, 'html.parser')
imptext = soup.find('div',class_='')
for data in imptext.find_all("a",href_= "/live-cricket-scores/137393/hk-vs-sla-7th-match-group-a-acc-mens-asia-cup-rising-stars-2025"):
    print(data.text)
print('_'*100)'''



import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-match/live-scores"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

live_links = []

# Find all live match boxes
match_boxes = soup.find_all("a", href=True)

for box in match_boxes:
    href = box["href"]

    # Only cricket live match links start with this:
    if href.startswith("/live-cricket-scores/"):
        full_link = "https://www.cricbuzz.com" + href
        if full_link not in live_links:
            live_links.append(full_link)

# Print final list
for link in live_links:
    print(link)
