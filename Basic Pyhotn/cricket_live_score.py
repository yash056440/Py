from bs4 import BeautifulSoup
import requests
import tempfile, os, threading
from gtts import gTTS
from playsound import playsound  # Faster than pygame

session = requests.Session()  # Speed booster

url = "https://www.cricbuzz.com/cricket-match/live-scores"
response = session.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# ================== Extract Live Links Fast ======================
section = soup.find('div', class_='flex flex-col gap-3 wb:mt-1 mt-3 wb:w-full wb:px-5')
links = section.select("a[href*='/live-cricket-scores/']")[:5]   # Direct filter (FAST)

live_links = ["https://www.cricbuzz.com" + a['href'] for a in links]
print(live_links)
print("-" * 80)

# ================== Extract Match Names ==========================
tm_name = []
for i, link in enumerate(live_links, start=1):
    s = BeautifulSoup(session.get(link).text, 'html.parser')
    title = s.select_one("div.flex.items-center.justify-between.wb\\:pr-6 h1")

    if title:
        print(i, title.text)
        tm_name.append(title.text)

print("-" * 80)

# ================== User Input Section ===========================
num = int(input("Enter match number to check score: "))

if 1 <= num <= len(live_links):
    sp = BeautifulSoup(session.get(live_links[num-1]).text,'html.parser')
    score_section = sp.select_one("div.w-3\\/5")

    if score_section:
        score_text = "\n".join([d.text.strip() for d in score_section.find_all("div")])
        print(score_text)
    else:
        print("Match Ended")
        exit()
else:
    print("Invalid Choice")
    exit()

# ================== Speech Function (FAST) ======================
def speak_fast(text):
    temp = tempfile.mktemp(suffix='.mp3')
    try:
        gTTS(text=text, lang="en").save(temp)   # Fast convert
        playsound(temp)                         # Faster playback
    finally:
        if os.path.exists(temp):
            os.remove(temp)

thread = threading.Thread(target=speak_fast,args=(score_text,), daemon=True)
thread.start()

while thread.is_alive():
    pass
