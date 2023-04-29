import requests
from bs4 import BeautifulSoup
import ffmpeg
import os
os.makedirs("output", exist_ok=True)
import sys
args = sys.argv

id = ""

try:
    id = args[1]
except:
    print("Error: No ID specified")


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
    stream = ffmpeg.input(video)
    stream = ffmpeg.output(stream, "output/{}.mp4".format(id), map="0:p:2", format="mp4")
    stream = ffmpeg.overwrite_output(stream)
    ffmpeg.run(stream)
except:
    import traceback
    traceback.print_exc()
    print("Error: Failed to download video")
    exit()