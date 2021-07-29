from concurrent.futures import ThreadPoolExecutor, as_completed
import concurrent
from time import sleep

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://www.bbc.co.uk/1',
        'http://www.bbc.co.uk/2',
        'http://www.bbc.co.uk/3',
        'http://www.bbc.co.uk/4',
        'http://www.bbc.co.uk/5',
        'http://www.bbc.co.uk/6',
        'http://www.bbc.co.uk/8',
        'http://www.bbc.co.uk/9',
        'http://www.bbc.co.uk/10',
        'http://www.bbc.co.uk/11',
        'http://www.bbc.co.uk/12',
        'http://some-made-up-domain.com/']


def load_url(url, timeout):
    # with urllib.request.urlopen(url, timeout=timeout) as conn:
    #     return conn.read()
    sleep(1)
    print(url)
    # if url == 'http://europe.wsj.com/':
    #     print('Raising exception')
    #     raise Exception
    

def main():
    # try:
    #     batch_size = 3
    #     with ThreadPoolExecutor(max_workers=batch_size) as executor:
    #         futures_list = {executor.submit(load_url, url, 60): url for url in URLS}
    #         executor = ''
    #         done, not_done = concurrent.futures.wait(futures_list, timeout=0)
    #         try:
    #             while not_done:
    #                 freshly_done, not_done = concurrent.futures.wait(not_done, timeout=2)
    #         except Exception:
    #             for future in not_done:
    #                 print('Cancel Future')
    #                 _ = future.cancel()
    #                 print('Wait Future not done')
    #                 _ = concurrent.futures.wait(not_done, timeout=None)
    # except Exception as e:
    #     print('exception caught', e)
        
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures_list = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in as_completed(futures_list):
            url = futures_list[future]
            print('-------------------')
            print(futures_list[future])
            print('-------------------')
            try:
                data = future.result()
            except Exception :
                print('Do non graceful termination')
                executor._threads.clear()
                concurrent.futures.thread._threads_queues.clear()
                raise

if __name__ == '__main__':
    main()
