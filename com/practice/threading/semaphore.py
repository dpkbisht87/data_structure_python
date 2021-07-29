class Semaphore:
    def __init__(self, premits):
        self.max_permits = premits
        self.given_out = 0
        self.cond_var = Condition()

    def acquire(self):
        cond_var.acquire()
        while self.given_out == self.max_permits:
            self.cond_var.wait()
        self.given_out += 1
        self.cond_var.notifyAll()
        self.cond_var.release()

    def release(self):
        cond_var.acquire()
        while self.max_permits == 0:
            self.cond_var.wait()

        self.given_out -= 1
        self.cond_var.notifyAll()
        self.cond_var.release()
