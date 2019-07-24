#Quick Sort
#Also uses divide and conquer, while not using additional storage like the merge sort. 
#The list may not be split in half, which will reduce performance in these scenarios. 
#First selects a "pivot value", which can be determined in many ways.
#Pivot value is used to help with splitting the list.
#The pivot value's final position in the final list is known as the split point, which will be used to divide the list for subsequent calls. 
#Next is partitioning, which finds the split point and moves other items to appropriate sides of the list, either greater than or less than the value.
#Locates two position markers at the beginning and end of the remaining items in the list. 
#This process should move items on the wrong side of the pivot value to the right side, while converging on the split point. 
#Left marker keeps moving right until the value of the marker is greater than the pivot value.
#Right marker keeps moving left until the value of the marker is less than the pivot value. 
#We can confirm that both of these values are on the wrong sides, and swap them. 
#Repeat this process until the rightmark crosses the leftmark. The split point is where the rightmark crosses, and the pivot value and rightmark are then swapped.
#A key point here is that now, all the values left of the split point are smaller than the pivot value, and all of the values right of the split point are larger than the pivot value. The function can be invoked recursively now on the two "halves".

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

      splitpoint = partition(alist,first,last)

      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
         leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
         rightmark = rightmark -1  

      if rightmark < leftmark:
         done = True
      else:
         temp = alist[leftmark]
         alist[leftmark] = alist[rightmark]
         alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

#If the split points are chosen well and exactly in the middle of the list, then the time is O(nlogn), without the use of memory like in the merge sort. However, in the worst case, which has a division of the original list into 0 items and n-1 items, and could go all the way down until only one term is left to be checked. In this case, the time is O(n^2). 
#The main problem is that the pivot value may result in very uneven divisions, so it is key to have a method to pick pivot values that can more consistently have good splits. 
#The median of 3 is a more consistent method to pick pivot values, especially when the list is already somewhat sorted. It takes the first, middle, and last values of the list, and picks the middle-sized one. 