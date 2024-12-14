import threading

def thread_code(tid):
    for i in range(0,4):
        print(tid, ": ", i)

threading.Thread(target=thread_code, args=('t1',)).start()
threading.Thread(target=thread_code, args=('t2',)).start()