from threading import Thread
from threading import Semaphore
import time
import random

class DiningPhilosopherProblem:

    def __init__(self):
        self.forks = [None] * 5
        self.forks[0] = Semaphore(1)
        self.forks[1] = Semaphore(1)
        self.forks[2] = Semaphore(1)
        self.forks[3] = Semaphore(1)
        self.forks[4] = Semaphore(1)
        self.exit = False

    def life_cycle_of_philosopher(self, id):
        while self.exit is False:
            self.contemplate()
            self.eat(id)

    def contemplate(self):
        sleep_for = random.randint(100, 500) / 1000
        time.sleep(sleep_for)

    def acquire_fork_for_right_handed_philosopher(self, id):
        self.forks[i].acquire();
        self.forks[(id + 1) % 5].acquire()

    def acquire_fork_for_left_handed_philosopher(self, id):
        self.forks[(id + 1) % 5].acquire()
        self.forks[i].acquire();

    def eat(self, id):
        if id is 3:
            self.acquire_fork_for_left_handed_philosopher(3)
        else:
            self.acquire_fork_for_right_handed_philosopher(id)

        # eat to your heart's content
        print("Philosopher {0} is eating".format(id))

        self.forks[id].release()
        self.forks[(id + 1) % 5].release()

if __name__ == '__main__':
    problem = DiningPhilosopherProblem()
    phil = list()

    for i in range(5):
        phil.append(Thread(target=problem.life_cycle_of_philosopher, args=(i,)))

    for thread in phil:
          thread.start()

    time.sleep(5)
    problem.exit = True

    for thread in phil:
          thread.join()