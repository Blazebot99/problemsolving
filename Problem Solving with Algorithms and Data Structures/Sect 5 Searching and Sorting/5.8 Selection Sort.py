#Selection Sort
#Improves on bubble sort by only exchanging once. 
#It looks for the largest value when passing, and after completing pass, places it in proper location. 
#After every pass, another item is put into the correct place, and so it makes a total of n-1 passes.

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
      positionOfMax=0
      for location in range(1,fillslot+1):
         if alist[location]>alist[positionOfMax]:
            positionOfMax = location

      temp = alist[fillslot]
      alist[fillslot] = alist[positionOfMax]
      alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

#Consequently, both bubble sort and selection sort are in O(n^2) time, but selection is faster as it makes far less exchanges. 