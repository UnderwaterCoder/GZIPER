import gzip
import os
import shutil
import sys

def select_files(files,folders,DATAINPUT_FOLDER_PATH,OUTPUT_FOLDER):
    print("[INFO]: SELECT ALL FILES")
    cache_folders = [INPUT_FOLDER]
    while True:
        for path in os.listdir(cache_folders[0]):
            if os.path.isdir(cache_folders[0]+"/"+path):
                cache_folders.append(cache_folders[0]+"/"+path)
                folders.append((OUTPUT_FOLDER+cache_folders[0]+"/"+path,path))
            else:
                print("[INFO]: Selected file ==> "+path)
                files.append((cache_folders[0]+"/"+path,path))

        if len(cache_folders) == 1:
            print("[INFO]: ALL FILES SELECTED")
            break

        cache_folders.pop(0)

def create_folders(folders):
    folder_created = False
    print("[INFO]: FOLDER CREATE PROCESS HAS BEN STARTED")
    for folder_path, folder_name in folders:
        try:
            os.mkdir(folder_path)
            print("[INFO]: Created folder ==> "+folder_name)
            folder_created = True
        except FileExistsError:
            pass
    
    if folder_created:
        print("[INFO]: ALL FOLDERS ARE CREATED")
    else:
        print("[WARN]: NO FOLDER ARE CREATED")

def gzip_process(files,OUTPUT_FOLDER):
    print("[INFO]: COMPRESSING HAS BEN STARTED")
    for file_path, file_name in files:
        with open(file_path, "rb") as file_in:
            with gzip.open(OUTPUT_FOLDER+file_path+".gz", "wb") as file_out:
                shutil.copyfileobj(file_in, file_out)
        print("[INFO]: Compressed file ==> "+file_name)
    print("[INFO]: ALL FILES ARE COMPRESSED")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print("[ERROR]: I NEED A INPUT AND A OUTPUT!")
    INPUT_FOLDER = sys.argv[1]
    OUTPUT_FOLDER = sys.argv[2]+"/"
    files = []
    folders = [(OUTPUT_FOLDER[:-1],OUTPUT_FOLDER[:-1]),(OUTPUT_FOLDER+INPUT_FOLDER,INPUT_FOLDER)]
    select_files(files,folders,INPUT_FOLDER,OUTPUT_FOLDER)
    create_folders(folders)
    gzip_process(files,OUTPUT_FOLDER)
