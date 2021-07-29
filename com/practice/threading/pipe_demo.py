from multiprocessing import Process, Pipe
import time

def child_process(conn):
    for i in range(10):
        conn.send('HI ' + str(i))
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(2)

    for i in range(10):
        msg = parent_conn.recv()
        print(msg)
    parent_conn.close()