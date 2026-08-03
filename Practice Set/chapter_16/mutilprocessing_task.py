import multiprocessing
import time



def task1():
    print("task1 is running")
    time.sleep(1)
    print("task1 is completed")

def task2():
    print("task2 is running")
    time.sleep(1)
    print("task2 is completed")

if __name__ == "__main__":

    t1 = multiprocessing.Process(target=task1)
    t2 = multiprocessing.Process(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main process completed")
