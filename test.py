from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=RWuUcYXAleM'

title = YouTube(url).streams[0].title
YouTube(url).streams.first().download('/Users/weichenho/Desktop/Python/youtube/movie')  #影片下載的路徑

download = os.listdir('/Users/weichenho/Desktop/Python/youtube/movie')                  #找到下載檔案的名稱

try:
    os.remove(f"/Users/weichenho/Desktop/Python/youtube/movie/.DS_Store")
except:
    pass
movie = download[0]

video = VideoFileClip(os.path.join("/Users/weichenho/Desktop/Python/youtube/movie", movie))    #要轉檔的位置
video.audio.write_audiofile(os.path.join("/Users/weichenho/Downloads",f"{movie}.mp3"))          #要存到哪裏的

os.remove(f"/Users/weichenho/Desktop/Python/youtube/movie/{movie}")	   #移除影片檔案


