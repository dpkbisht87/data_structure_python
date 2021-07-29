from threading import Semaphore, Thread, Condition

class BarberShop:
    def __init__(self):
        self.capacity = 5
        self.customers = 0
        self.chairs = [None] * 5
        self.chair = Semaphore(5)

        self.exit = False
        self.cond = Condition()
        self.barber = Lock()

    def customer_walks_in():
        self.cond.acquire()
        if self. capacity = self.customers:
            pass
        self.customers += 1
        elif self.customers == 0:
            self.barber.notify()
            self.chair.acquire()
        else:
            sel.chair.acquire(  )


    def barber(self):
        while not self.exit:
            self.barber.wait()
        self


if __name__ == '__main__':
