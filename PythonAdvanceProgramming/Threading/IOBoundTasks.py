#IO bound tasks
# IO bound tasks
'''

An I/O-bound task is a task where:

The program waits for data from external resources

CPU is mostly idle while waiting

Performance is limited by disk, network, or database speed

Examples of external resources:

Files

Network requests

Databases

APIs

User input

'''
import time

#example - without using the threading concept
def task():
    print("Task Started")
    time.sleep(3)
    print("Task Completed")
task()
task()

#total time taken 6 seconds

import threading

#multiple tasks concurrently within a single process.
#Threads share the same memory space of the process.
#This allows faster communication between them.

def task():
    print("Task Started")
    time.sleep(3)
    print("Task Completed")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

#fetch the api details
def fetch_data(api_name):
    print(f"fetching data from {api_name}")
    time.sleep(3)
    print(f"Completed {api_name}")

apis=["API1","API2","API3"]

threads = []
for api in apis:
    t=threading.Thread(target=fetch_data, args=(api,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All the API calls completed")

#file reading
def read_file(filename):
    with open(filename,"r") as f:
        data = f.read()
        print(f"{filename} read completed")

files = ["file1.txt","file2.txt"]


for files in files:
    t = threading.Thread(target=read_file, args=(files,))
    t.start()


for t in threads:
    t.join()


