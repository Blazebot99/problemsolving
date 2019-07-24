#Shell Sort AKA "Diminishing Increment Sort"
#Improves on insertion sort by breaking original list into a number of small sublists instead of just one.
#Essentially taking terms at an increment, or "gaps", and making smaller lists out of those to sort. 
#Ends off with a standard insertion sort, but is far faster due to the shell sort performed. 

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
  
        print("After increments of size",sublistcount,
                                     "The list is",alist)
  
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

