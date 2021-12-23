from threading import Thread,Event
import time
def thread1(my_event):
    print("111111111")
    for i in range(1,7):
        if i==4:
            my_event.set()
        print(i)
        time.sleep(1)
if __name__ == '__main__':
    my_event=Event()
    t=Thread(target=thread1,args=(my_event,))
    t.start()
    my_event.wait()
