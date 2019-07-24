#Merge Sort
#Uses a divide and conquer strategy to improve performance of sorting algorithms.
#Merge sort is a recrusive algorithm continually splitting a list in half. If the list is empty, or has one item, it is already sorted. 
#If the list has more than one item, it is split once more until reaching the base case (only one item or empty). 
#Known as "merge sort" because the sublists must be merged until the final list is put together. 

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

#Is in O(nlogn) time as we can split a list into half logn times. 