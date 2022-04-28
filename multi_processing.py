import multiprocessing
import threading
import time

def perform_multiprocessing():
    process_one = multiprocessing.Process(target=add_to_list)
    s = time.time()
    process_one.start()
    process_one.join()
    e = time.time()
    print("time taken..", e-s)

def add_to_list():
    thread_one = threading.Thread(target=print_odd_numbers)
    thread_two = threading.Thread(target=print_even_numbers)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()

def print_odd_numbers():
    print("t1")
    odd_list = []
    for i in range(10000):
        if i % 2 == 1:
            odd_list.append(i)
    print(odd_list)

def print_even_numbers():
    even_list = []
    print("t2")
    for i in range(10000):
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)

if __name__ == "__main__":
    perform_multiprocessing()




