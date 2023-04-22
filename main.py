import requests
from bs4 import BeautifulSoup
import ffmpeg
import os
os.makedirs("output", exist_ok=True)


#여기에 영상 ID를 입력하십시오. (례: ije220917004)
id = ""


url = f"http://www.vok.rep.kp/hls/player/{id}"

r = requests.get(url)

if r.status_code != 200:
    print("Error: {}".format(r.status_code))
    exit()

try:
    soup = BeautifulSoup(r.content, 'html.parser')
    video = soup.find('body').find('video').find('source')['src']
except:
    import traceback
    traceback.print_exc()
    print("Error: Video not found from HTML")
    exit()

print("Video URL: {}".format(video))
print("Downloading...")
try:
    ffmpeg.input(video).output("output/{}.mp4".format(id)).run()
except:
    import traceback
    traceback.print_exc()
    print("Error: Failed to download video")
    exit()