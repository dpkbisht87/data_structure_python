from multiprocessing import Process, Queue, current_process
import multiprocessing, sys
import random
from threading import Thread
from threading import Condition
import time
import threading
import Lock

def child_process(q):
    count = 0
    lock.acquire()
    while not q.empty():
        print(q.get())
        count += 1
        lock.notify()
    lock.release()

    print("child process {0} processed {1} items from the queue".format(threading.current_thread().name, count))

if __name__ == '__main__':
    # multiprocessing.set_start_method("forkserver")
    q = Queue()
    # print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    lock = Lock()
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Thread(target=child_process, args=(q,))
    p2 = Thread(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()