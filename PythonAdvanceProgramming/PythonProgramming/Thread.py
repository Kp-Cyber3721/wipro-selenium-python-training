# threading - execution of tasks
# multithreading - execution of many task at same time - concurrent execution-
# multiprocessing -
#threading-imported


#process - execution unit
import threading
import  time
def task ():
    print("thread started")
    time.sleep(2)
    print("thread finished")
t= threading.Thread(target=task)
t.start()
t.join()
print("Thread terminated")



