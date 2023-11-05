# Python implementation QuickSort using 
# Lomuto's partition Scheme.
import random
import time
from memory_profiler import profile

 
#quicksort (recursive)
def quicksort(array, start , stop):
    if(start < stop):
        pivotindex = partitionrand(array, start, stop)
         
        quicksort(array , start , pivotindex-1)
        quicksort(array, pivotindex + 1, stop)
    return array
 
#generate random partition 
def partitionrand(array , start, stop):
 
    randpivot = random.randrange(start, stop)

    array[start], array[randpivot] = array[randpivot], array[start]
    return partition(array, start, stop)
 
#quicksort using the start as pivot
def partition(array,start,stop):
    pivot = start 
     
    i = start + 1
    for j in range(start + 1, stop + 1): 
        if array[j] <= array[pivot]:
            array[i] , array[j] = array[j] , array[i]
            i = i + 1
    array[pivot] , array[i - 1] =\
            array[i - 1] , array[pivot]
    pivot = i - 1
    return (pivot)
 
@profile
def main(dataset):
    sorted = quicksort(dataset, 0, len(dataset)-1)
    return sorted


if __name__ == "__main__":

    txt_file_name = "d_200_reversed.txt"
    dataset = []

    #open and read the text file
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            number = int(line.strip()) 
            dataset.append(number)

    #run sorting and calculate the run time
    start_time = time.time()
    sorted = main(dataset)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")

    #write the sorted array in txt format
    with open("output_quicksort_200_reversed.txt", 'w') as txt_file:
        for value in dataset:
            txt_file.write(str(value) + '\n')