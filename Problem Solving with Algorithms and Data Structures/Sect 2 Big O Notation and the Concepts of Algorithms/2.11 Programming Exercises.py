"ONE"
def index_test():
    import timeit
    l=[i for i in range(100)]
    for i in range(100):
        t=timeit.Timer()
        a=l[i]
        end=t.timeit()
        print(end)

#This is a test devised to verify that the list type's index operator is constant. The test returns a time difference of about 0 regardless of the index, showing that it is indeed constant. 
#index_test()

"TWO"
def get_test():
    import timeit
    d={i:None for i in range(100)}
    for i in range(100):
        t=timeit.Timer()
        a=d.get(i)
        end=t.timeit()
        print(end)

#get_test()

def set_test():
    import timeit
    d={i:None for i in range(100)}
    for i in range(100):
        t=timeit.Timer()
        d[i]=0
        end=t.timeit()
        print(end) 
        
#set_test()

"THREE"
def del_test():
    import timeit
    l=[i for i in range(100)]
    d={i:None for i in range(100)}
    for i in range(100):
        t=timeit.Timer()
        del l[i]
        lt=t.timeit()
        del d[i]
        dt=t.timeit()        
        print(lt, "\t", dt)
        
#del_test()
#From this test, it can be ascertained that the del operator is constant on both lists and dicts.        

"FOUR"
def r_min(l, place=1):
    place-=1
    l.sort()
    return l[place]

l=[5,7,19,12034,29,3049,1]
arr = [1, 23, 12, 9, 30, 2, 50]

print(r_min(arr, 6))

"FIVE"
def r_min_opt(l, place=1):
    m=[]
    i=0
    while place>0:
        place-=1
        m.append(l[i])
        i+=1
    for i in l[i+1:]:
        for x in m:
            if i>x:
                m.index(x)==i
    return max(m)

print(r_min_opt(arr, 6))

    
            
    
            
        
    