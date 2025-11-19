import requests
from bs4 import BeautifulSoup

livescore = "https://www.cricbuzz.com/live-cricket-scores/134408/pak-vs-zim-1st-match-pakistan-t20i-tri-series-2025"

req = requests.get(livescore)
soup = BeautifulSoup(req.text, "html.parser")

  
title = soup.find("h1")
if title:
   
    teams = title.text.split("-")
    if len(teams) >= 2:
        team1 = teams[0].strip()
        team2 = teams[1].replace("vs", "").split(",")[0].strip()
        print(f"{team1} - {team2}")
    else:
        print("Team names not found in header.")
else:
    print("Title header not found.")
