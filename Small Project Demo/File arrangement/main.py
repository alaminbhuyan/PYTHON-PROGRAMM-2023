import os
import shutil

path = input("Enter your path: ")

for i in os.listdir(path=path):
    filename, extension = os.path.splitext(i)
    extension = extension[1:]
    folder_path = path + '\\' + extension + " files"
    source = path + '\\' + i
    if os.path.exists(path=folder_path):
        shutil.move(src=source, dst=folder_path + '\\' + i)
    else:
        os.mkdir(path=folder_path)
        shutil.move(src=source, dst=folder_path + '\\' + i)
