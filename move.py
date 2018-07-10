import shutil
import os
#works on windows 10
folders = ("desktop", "documents", "downloads", "music", "pictures", "videos")
fileTypes = ("images", "videos", "audio", "documents")
extensions = {"images": (".jpg", ".gif", ".png"), "videos": (".avi", ".flv", ".wmv", ".mov", ".mp4"), "audio": (".wav", ".mp3", ".wma", ".ogg"), "documents": (".doc", ".txt", ".pdf", ".rtf", ".sxw", ".stw") }

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
