#v.0.0.1
import shutil
import os
#works on windows 10

folders = ("desktop", "documents", "downloads", "music", "pictures", "videos")
fileTypes = ("images", "videos", "audio", "documents")
#https://fileinfo.com/filetypes/common
extensions = {"images": (".jpg", ".gif", ".png", ".tiff", ".tif", ".yuv", ".thm", ".tga", ".pspimage", ".psd", ".dds", ".bmp"), "videos": (".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob", ".wmv"), "audio": (".wav", ".mp3", ".mpa", ".wma", ".ogg", ".mid", ".m4a", ".m3u", ".iff", ".aif"), "documents": (".doc", ".docx", ".log", ".msg", ".otd", ".pages", ".rtf", ".tex", ".txt", ".pdf", ".wpd", ".wps", ".sxw", ".stw", ".csv", ".dat", ".pps", ".ppt", ".pptx", ".xlr", ".xls", ".xlsx", ".indd", ".pct", ".ai", ".eps", ".ps", ".svg") }

def getItem(items, message):
    print(message)
    tmp = input( str(items)[1:-1] + "\n" )
    while(not tmp.lower() in items):
        print("not found")
        print(message)
        tmp = input( str(items)[1:-1] + "\n" )
    return tmp


sourceFolder = getItem(folders, "Which folder would you like to move from?")
destFolder = getItem(folders, "Which folder would you like to move to?") 

source = "C:/Users/" + os.getlogin() + "/" + sourceFolder + "/"
dest = "C:/Users/" + os.getlogin() + "/" + destFolder + "/"

fileType = getItem(fileTypes, "Which type of file would you like to move?")

print("moving files")
moved = 0

files = os.listdir(source)
for f in files:
    if os.path.splitext(f)[1] in extensions[fileType]:
        shutil.move(source + f, dest)
        print("\t" + os.path.splitext(f)[0] + os.path.splitext(f)[1])
        moved += 1

print("moved " + str(moved) + " files")
