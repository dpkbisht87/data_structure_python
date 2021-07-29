from threading import *
import time

list1 = [1,2,3,4,5]
my_lock = Lock()

def read_operation():
    my_lock.acquire()
    print(list1)
    my_lock.release()

def write_operation():
    my_lock.acquire()
    time.sleep(3)
    list1[2] = 333
    my_lock.release()


if __name__ == '__main__':
    print('Hello World')
    t1 = Thread(target=read_operation, name='read_thread')
    t2 = Thread(target=write_operation, name='write_thread')

    t2.start()
    t1.start()

    t1.join()
    t2.join()

    print(list1)
    
#
lock = Lock()
cond_var = Condition(lock)
cond_var.acquire()
cond_var.wait()    