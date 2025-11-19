import requests
from bs4 import BeautifulSoup

livescore = "https://www.cricbuzz.com/live-cricket-scores/124629/tn-vs-up-elite-group-a-ranji-trophy-elite-2025-26"

req = requests.get(livescore)
soup = BeautifulSoup(req.text, "html.parser")

# Find team names
team_blocks = soup.find_all("div", class_="cb-min-bat-rw")
teams = []

for block in team_blocks:
    name = block.find("div", class_="cb-min-itm-rw")
    if name:
        teams.append(name.text.strip())

# Print only 1 match team names
if len(teams) >= 2:
    print("Team 1:", teams[0])
    print("Team 2:", teams[1])
else:
    print("Team names not found.")

    
   