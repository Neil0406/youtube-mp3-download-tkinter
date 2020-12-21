from moviepy.video.io.VideoFileClip import VideoFileClip
import os

data = os.listdir('/Users/weichenho/Desktop/Python/youtube/movie')
print(data[1][:-4])

# video = VideoFileClip(os.path.join("/Users/weichenho/Desktop/Python/youtube/movie", f"{movie}.mp4"))    #要轉檔的位置
# video.audio.write_audiofile(os.path.join("/Users/weichenho/Downloads",f"{movie}.mp3"))          #要存到哪裏的

# os.remove(f"/Users/weichenho/Desktop/Python/youtube/movie/{movie}.mp4")	   #移除影片檔案