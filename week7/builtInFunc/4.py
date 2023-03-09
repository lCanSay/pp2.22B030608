import math
import time
a=int(input())
t=float(input())
time.sleep(t/1000)
print("Square root of {} after {} miliseconds is {}".format(a,t,math.sqrt(a)))
