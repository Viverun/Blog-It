import time
def usingwhile():
    i = 0
    while i<500000:
        i = i + 1
        print(i)
def usingfor():
    for j in range(50000):
        print(j)
init = time.time()
usingfor()
t1 = time.time()-init
init = time.time()
usingwhile()
t2 = time.time()-init
print(t1)
print(t2)