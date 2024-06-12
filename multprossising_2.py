import multiprocessing
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


if __name__ == '__main__':
    # Ikki jarayon (process) yaratiladi va ishga tushiriladi
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
