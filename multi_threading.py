from threading import Thread
import time


# def a function that will run in a threadto be executed in a thread
def time_counter():
    counter = 0
    while True:
        print(time.ctime(time.time()))
        time.sleep(1)
        counter += 1
        print(f"Time counter: {counter}")

time_counter_thread = Thread(target=time_counter, daemon=True))
time_counter_thread.start()


stop = input("Press enter to stop the thread: ")