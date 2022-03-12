from threading import *
import time

class Apple(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('Apple')

class Mango(Thread):
    def run(self):
        for x in range(10):
            time.sleep(1)
            print('Mango')


apple_obj = Apple()
mango_obj = Mango()

start_time = time.perf_counter()

apple_obj.start()
time.sleep(0.1)
print("")
mango_obj.start()
time.sleep(0.1)
apple_obj.join()
mango_obj.join()

end_time = time.perf_counter()

print(round(end_time - start_time))





