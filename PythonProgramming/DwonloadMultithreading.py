import threading
import time

def download_file(file_name):
    print(("Downloading the file"))
    time.sleep(2)
    print(f"{file_name} downloaded")

files = ["file.txt" , "files2.txt" , "files3.txt"]

threads = [threading.Thread(target=download_file,args = (file,)) for file in files]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


