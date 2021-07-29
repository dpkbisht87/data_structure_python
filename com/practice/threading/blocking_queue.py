from threading import Thread
from threading import Condition
from threading import current_thread
import time
import random

class BlockingQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cur_size = 0
        self.cond = Condition()
        self.q = []

    def enqueue(self, item):
        self.cond.acquire()
        while self.cur_size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        self.cur_size += 1
        self.cond.notifyAll()
        print("\ncurrent size of queue {0}".format(self.cur_size))
        self.cond.release()

    def dequeue(self):
        self.cond.acquire()
        while self.cur_size == 0:
            self.cond.wait()

        self.q.pop(0)
        self.cur_size -= 1
        self.cond.notifyAll()
        self.cond.release()

def consumer_thread(blocking_q):
    while 1:
        item = blocking_q.dequeue()
        print("\n{0} consumed item {1}".format(current_thread().getName(), item), flush=True)
        time.sleep(random.randint(1, 3))

def producer_thread(blocking_q, item):
    while 1:
        blocking_q.enqueue(item)
        time.sleep(0.1)


if __name__ == '__main__':
    blocking_q = BlockingQueue(5)

    consume_t1 = Thread(target=consumer_thread, name="consumer-1", args=(blocking_q,), daemon=True)
    consume_t2 = Thread(target=consumer_thread, name="consumer-2", args=(blocking_q,), daemon=True)
    producer_p1 = Thread(target=producer_thread, name="producer-1", args=(blocking_q, 2), daemon=True)
    producer_p2 = Thread(target=producer_thread, name="producer-2", args=(blocking_q, 100), daemon=True)

    consume_t1.start()
    consume_t2.start()
    producer_p1.start()
    producer_p2.start()

    time.sleep(12)
    print('Main thread exiting')