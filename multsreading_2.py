import threading
import time


def print_numbers():
    time.sleep(1)
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)


def print_letters():
    time.sleep(1)
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)


# Ikki vazifa (thread) yaratiladi va ishga tushiriladi
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()


