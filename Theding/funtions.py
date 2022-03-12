import time
from threading import *


def pevnes(num):
    # print(f'printing evens nums upto : {num}')
    for x in range(num):
        time.sleep(0.1)
        if x % 2 == 0:
            print(x)


def podd(num):
    # print(f'printing odd nums upto : {num}')
    for x in range(num):
        time.sleep(0.1)
        if x % 2 == 1:
            print(x)


str_time = time.perf_counter()
evens = Thread(target=pevnes, args=(100,))
odds = Thread(target=podd, args=(100,))
evens.start()
odds.start()
evens.join()
odds.join()
end_time = time.perf_counter()
print("time taken = ", round(end_time - str_time), "Seconds")
input()
