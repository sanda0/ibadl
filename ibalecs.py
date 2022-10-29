from os import link
from vimeo_downloader import Vimeo
from tkinter import filedialog

help = """
+----------------------------------------+
|              > ibadl <                 | 
|  (IBA Campus Lecturers Downloader)     |
| link : https://github.com/sanda0/ibadl |   
|                v1.0                    |
| (Author : https://github.com/sanda0)   |
+----------------------------------------+

1 . Dowloader
2 . exit

------------------------------------------
"""


def download(v_list,i):
    # print(i)
    f = filedialog.asksaveasfilename(typevariable=".mp4")
    print(f)
    v_list[i].download(filename=str(f))
    print("Downloade Completed :)\n\n ")
    print("------------------------------------------")

def convert():
    # https://www.iba.lk/new/play_video.php?link=https://player.vimeo.com/video/756692472&vid=13885
    link = input("Enter video link : ")
    link = link.split("&vid")[0].replace(" ","")
    link_p1 = link.split("link=")[0]+"link="
    link_p2 = link.split("link=")[1]

    print("\nConverting...")
    vimeo = Vimeo(link_p2,embedded_on=link_p1)
    v_list = vimeo.streams
    print("Select video type to download ")    

    for i in range(len(v_list)):
        print("\t",i+1," : "+str(v_list[i]).replace("Stream","").replace("(","").replace(")",""))
        

    v_type = int(input("video type : "))
    if v_type > 0 and v_type <= len(v_list):
        download(v_list,v_type-1)
    else:
        print("please select valid video type")


while True:
    print(help)
    s = int(input("Select opption >>> "))
    if s == 2:
        break

    
    elif s == 1:
        convert()

    else:
        print("invalid selection\n\n")
        

    


        


