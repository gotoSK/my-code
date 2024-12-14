import threading
import time

lock = threading.Lock()

def thread_code(tid):
    with lock:
        for i in range(0,4):
            print(tid, ": ", i)
            time.sleep(1);

threading.Thread(target=thread_code, args=('t1',)).start()
threading.Thread(target=thread_code, args=('t2',)).start()