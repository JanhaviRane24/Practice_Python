import threading
import time

def task1():
    print("task1 is running")
    time.sleep(1)
    print("task1 is completed")

def task2():
    print("task2 is running")
    time.sleep(1)
    print("task2 is completed")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t1.join()

t2.start()

t2.join()

