# Python implementation QuickSort using 
# Lomuto's partition Scheme.
import random
import time
from memory_profiler import profile

 
'''
The function which implements QuickSort.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
def quicksort(arr, start , stop):
    if(start < stop):
        pivotindex = partitionrand(arr, start, stop)
         
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
    return arr
 
# This function generates random pivot,
# swaps the first element with the pivot 
# and calls the partition function.
def partitionrand(arr , start, stop):
 
    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)
 
'''
This function takes the first element as pivot, 
places the pivot element at the correct position 
in the sorted array. All the elements are re-arranged 
according to the pivot, the elements smaller than the
pivot is places on the left and the elements
greater than the pivot is placed to the right of pivot.
'''
def partition(arr,start,stop):
    pivot = start 
     
    i = start + 1
     
    for j in range(start + 1, stop + 1): 
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
 
@profile
def main(dataset):
    sorted = quicksort(dataset, 0, len(dataset)-1)
    return sorted

# Driver Code
if __name__ == "__main__":

    txt_file_name = "d_20000_sorted.txt"
    dataset = []

    # Open and read the text file
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            number = int(line.strip()) 
            dataset.append(number)


    start_time = time.time()
    sorted = main(dataset)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")
