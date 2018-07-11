#todo: add list files option. list different file types
#list file extensions for specific type of files
#add exit as an option in more places
import shutil
import os
from pathlib import Path
#works on windows 10
version = "0.0.2"
options = ("move files", "file extensions", "clean desktop", "about", "exit")
folders = ("desktop", "documents", "downloads", "music", "pictures", "videos")
fileTypes = ("images", "videos", "audio", "documents")
#https://fileinfo.com/filetypes/common
extensions = {"images": (".jpg", ".gif", ".png", ".tiff", ".tif", ".yuv", ".thm", ".tga", ".pspimage", ".psd", ".dds", ".bmp"), "videos": (".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob", ".wmv"), "audio": (".wav", ".mp3", ".mpa", ".wma", ".ogg", ".mid", ".m4a", ".m3u", ".iff", ".aif"), "documents": (".doc", ".docx", ".log", ".msg", ".otd", ".pages", ".rtf", ".tex", ".txt", ".pdf", ".wpd", ".wps", ".sxw", ".stw", ".csv", ".dat", ".pps", ".ppt", ".pptx", ".xlr", ".xls", ".xlsx", ".indd", ".pct", ".ai", ".eps", ".ps", ".svg") }

cleanDesktop = {"pictures":"images", "videos":"videos", "music":"audio", "documents":"documents"}

def getItem(items, message):
    print(message)
    tmp = input( str(items)[1:-1] + "\n" )
    while(not tmp.lower().strip() in items):
        print("not found")
        print(message)
        tmp = input( str(items)[1:-1] + "\n" )
    return tmp.lower().strip()


def moveFiles(source, dest, fileType):
    moved = 0
    files = os.listdir(source)
    for f in files:
        if os.path.splitext(f)[1].lower() in extensions[fileType]:
            shutil.move(source + f, dest)
            print("\t" + os.path.splitext(f)[0] + os.path.splitext(f)[1])
            moved += 1

    return moved



option = getItem(options, "What would you like to do?")
while option != "exit":
    if option == "move files":
        sourceFolder = getItem(folders, "Which folder would you like to move from?")
        destFolder = getItem(folders, "Which folder would you like to move to?") 

        source = str(Path.home()) + "/" + sourceFolder + "/"
        dest = str(Path.home()) + "/" + destFolder + "/"

        fileType = getItem(fileTypes, "Which type of file would you like to move?")

        print("moving files...")
        moved = moveFiles(source, dest, fileType)
        print("moved " + str(moved) + " files")

    elif option == "file extensions":
        print(extensions)

    elif option == "clean desktop":
        source = str(Path.home()) + "/desktop/"
        print("moving files...")
        moved = 0
        for key, value in cleanDesktop.items():
            #keys are folders, values are fileTypes
            dest = str(Path.home()) + "/" + key + "/"
            fileType = value
            moved += moveFiles(source, dest, fileType)
        print("moved " + str(moved) + " files")

    elif option == "about":
        print("\tpymove version " + version)
        print("\twindows only")
        print("\tuse pymove to easily move different types of files between folders")

    option = getItem(options, "What would you like to do?")

