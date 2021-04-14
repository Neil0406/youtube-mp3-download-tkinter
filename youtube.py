from pytube import YouTube
import os
import tkinter as tk
from moviepy.video.io.VideoFileClip import VideoFileClip

window = tk.Tk()
window.title('Youtube轉檔')
window.geometry('400x200')
window.configure(background='white')

def url():
    url = str(url_entry.get())
    # title = YouTube(url).streams[0].title
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

    result1_label.configure(text=f'{movie}')
    result_label.configure(text='下載完成')
#-----------------------tkbox---------------------------


#TOP title
header_title = tk.Label(window, text='Youtube轉mp3')
header_title.pack()

search_frame = tk.Frame(window)                                
search_frame.pack(side=tk.TOP)                              
search_label = tk.Label(search_frame, text='影片網址：')      
search_label.pack(side=tk.LEFT)                                        
url_entry = tk.Entry(search_frame)                          
url_entry.pack(side=tk.LEFT)                               

#BTN
top_btn_frame = tk.Frame(window)
top_btn_frame.pack(side=tk.TOP)

url_btn = tk.Button(top_btn_frame, text='下載', fg='red',command= url)
url_btn.pack(side=tk.LEFT)

result1_label = tk.Label(window)
result1_label.pack()

result_label = tk.Label(window)
result_label.pack()



window.mainloop()
