#Insertion Sort
#Still O(n^2), but maintains a sorted sublist in the lower positions of the list. 
#Every item in the list is inserted back into the smaller sublist so that the sorted one is one item larger, until the list is fully "refreshed".
#Assume the first term is a list of length one and is already sorted.
#After that, for each term in the smaller list, check if the item is greater than every subsequent term, and when it is, insert the item.
#In benchmarks, insertion sort has quite good performance because on average, a shift operation is a third of the work of an exchange. 

def insertionSort(alist):
   for index in range(1,len(alist)):

      currentvalue = alist[index]
      position = index
 
      while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
 
      alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

