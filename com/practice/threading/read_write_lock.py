class ReadersWriteLock:
    def __init__(self):
        self.cond = Condition()
        self.write_in_progress = False
        self.readers = 0

    def acquire_read_lock(self):
        self.cond.acquire()
        while self.write_in_progress:
            self.cond.wait()

        self.readers += 1
        self.cond.release()

    def acquire_write_lock(self):
        self.cond.acquire()
        while self.write_in_progress or self.reader is not 0:
            self.cond.wait()
        self.write_in_progress = True
        self.cond.release()

    def release_read_lock(self):
        self.cond.acquire
        self.readers -= 1
        if self.readers == 0:
            self.cond.notifyAll()
        self.cond.release()

    def release_write_lock(self):
        self.cond.acquire()
        self.write_in_progress = False
        self.cond.notifyAll()
        self.cond.release()