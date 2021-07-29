from threading import Thread
from threading import current_thread
from threading import Semaphore
from threading import current_thread
from threading import Lock
from threading import Barrier
import random
import time

class TokenBucketFilter:
    def __init__(self, MAX_TOKENS):
        self.MAX_TOKENS = MAX_TOKENS
        self.possible_tokens = 0
        self.last_requested_time = time.time()
        self.lock = Lock()

    def getToken(self):
        with self.lock:
            self.possible_tokens += int(time.time() - self.last_requested_time)

            if self.possible_tokens == 0:
                sleep(1)
            else:
                self.possible_tokens -= 1

            self.last_requested_time = time.time()
            print("Granting {0} token at {1} ".format(current_thread().getName(), int(time.time())));



if __name__ == "__main__":
    token_bucket = TokenBucketFilter()

    threads = list()
    for i in range(10):
        threads.append(Thread(target=token_bucket_filter.getToken()))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
