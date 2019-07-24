import time
def min_one(l):
    start=time.time()
    smallest=l[0]
    for a in l:
        for b in l:
            if b<smallest:
                smallest=b
    end=time.time()
    return smallest, end-start


def min_two(l):
    start=time.time()
    smallest=l[0]
    for n in l[1:]:
        if n<smallest:
            smallest=n
    end=time.time()
    return smallest, end-start

s=[]                
for i in range(1, 10000):
    s.append(i)

print(min_one(s))
print(min_two(s))

