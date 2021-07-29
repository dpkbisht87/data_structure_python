from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def say_hi(item):
    print("\nhi " + str(item) + " executed in thread id " + current_thread().name)

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)
    lst = list()
    for i in range(10):
        list.append(executor.submit(say_hi, 'Guest'+ str(i)))

    for future in lst:
        future.result()

    executor.shutdown()