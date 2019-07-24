import time

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

#popzero, or popping with an index, is significantly slower than just popping from a list. This is because popping with an index requires the list to be traversed to find the exact object at the index, while a regular pop just removes and returns the last item in the list.  
popzero = timeit.Timer("x.pop(0)",
                      "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
popzero.timeit(number=1000)
4.8213560581207275

x = list(range(2000000))
popend.timeit(number=1000)
0.0003161430358886719