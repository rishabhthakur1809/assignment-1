#Question1
import threading
from threading import Thread
import time
class Th(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        time.sleep(5)
        print("hello i am running",self.h)
obj1 = Th(1)
obj1.start()
obj2 = Th(2)
obj2.start()


#Question 2

import threading
from threading import Thread
import time
class Th(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):

        print("Number is = ", self.h)

for i in range(1,11):
    thread = Th(i)
    time.sleep(1)
    thread.start()


#Question 3
import threading
from threading import Thread
import time

List = [1, 4, 6, 8, 9]
class Data(threading.Thread):


    def __init__(self, i):
         threading.Thread.__init__(self)
         self.h = i

    def run(self):
         print("Number is = ", self.h)

for i in List :
     for f in range(2,11,2):
            thread = Data(i)
            time.sleep(f)
            print(f)
            thread.start()



#Question 4
import math
import threading
from threading import Thread
import time
class Th(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
       print(math.factorial(5))

obj1 = Th(1)
obj1.start()
