from bs4 import BeautifulSoup
import requests
import os
import tempfile
import threading
#download module



url = "https://www.cricbuzz.com/cricket-match/live-scores"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

mytext = soup.find('div',class_='flex flex-col gap-3 wb:mt-1 mt-3 wb:w-full wb:px-5')
all_links = mytext.find_all("a", href=True)

live_links = []                  


     
for tag in all_links:
    href = tag["href"]
    if "/live-cricket-scores/" in href:    
        full_link = "https://www.cricbuzz.com" + href      # Generate link = .....+ href logic(Ai)
    
        if full_link not in  live_links:                   # not in (Ai)
                live_links.append(full_link)
    
    if len(live_links)>4:
        break  
                                   
#print(live_links)
#print("-"*100)

c=1
tm_name = [] 

for i in live_links:
    r = requests.get(i)
    s = BeautifulSoup(r.text, 'html.parser')
    imptext = s.find('div',class_='flex items-center justify-between wb:pr-6')

    
    for data in imptext.find_all('h1'):
            
            print(c,data.text)
            c +=1
            tm_name.append(data)
        
print("-"*90)   
num = int(input("Enter match number which you want to watch : "))
print("-"*90)

if num >=1 and num<=5:
      
    req = requests.get(live_links[num -1])
    sp = BeautifulSoup(req.text,'html.parser')
    stxt = sp.find('div',class_ ='w-3/5')   
              
    if stxt is None:                                # none (Ai)
        print("Match ended")
    else:
        score = "\n".join([d.text.strip() for d in stxt.find_all("div")])
        print(score)
        text = score
else:
    print("Invalid")
    exit()


print("-"*90)
import pygame
from gtts import gTTS

def speak(text, lang="en", slow=False):
    temp_file = tempfile.mktemp(suffix='.mp3')
    
    try:
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(temp_file)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pass

        print("\n✔ Score Speaking Completed")

    except Exception as e:
        print("TTS Error:", e)
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


thread = threading.Thread(target=speak,args=(text,),daemon=True)
thread.start()

                                                            # Keep program running until speech completes
while thread.is_alive():
    pass
