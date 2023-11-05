import time
import random
from memory_profiler import profile

def binary_loc_finder(a_list, start, end, key):
  if start == end:
    if a_list[start] > key:
      loc = start
      return loc
    else:
      loc = start+1
      return loc
    
  if start>end:
    loc = start
    return loc
  else:
    middle = (start+end)//2
    if a_list[middle] < key:
      return binary_loc_finder(a_list, middle+1, end, key)
    elif a_list[middle] > key:
      return binary_loc_finder(a_list, start, middle-1, key)
    else:
      return middle
    
def place_inserter(a_list, start, end):
  temp = a_list[end]
  for k in range(end, start-1, -1):
    a_list[k] = a_list[k-1]
    k = k-1
  a_list[start] = temp
  return a_list

@profile
def cbis(a_list):
  cop = 0
  pop = 0
  for i in range(1,len(a_list)):
    cop = i
    key = a_list[cop]
    if key>=a_list[pop]:
      place = binary_loc_finder(a_list, pop+1, cop-1, key)
    else:
      place = binary_loc_finder(a_list, 0, pop-1, key)
    pop = place
    a_list = place_inserter(a_list, place, cop) 
  
  return a_list


if __name__ == "__main__":
    txt_file_name = "d_20000_reversed.txt"
    dataset = []

    # Open and read the text file
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            number = int(line.strip()) 
            dataset.append(number)
  
    start_time = time.time()
    sorted = cbis(dataset)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")
