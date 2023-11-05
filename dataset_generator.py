import random

d_200_random = [random.randint(1, 200) for _ in range(200)]
with open("d_200_random.txt", 'w') as txt_file:
    for value in d_200_random:
        txt_file.write(str(value) + '\n')

d_200_sorted = [i for i in range(1,201)]
with open("d_200_sorted.txt", 'w') as txt_file:
    for value in d_200_sorted:
        txt_file.write(str(value) + '\n')

d_200_reversed = [200-i for i in range(1,201)]
with open("d_200_reversed.txt", 'w') as txt_file:
    for value in d_200_reversed:
        txt_file.write(str(value) + '\n')


d_2000_random = [random.randint(1, 2000) for _ in range(2000)]
with open("d_2000_random.txt", 'w') as txt_file:
    for value in d_2000_random:
        txt_file.write(str(value) + '\n')
        
d_2000_sorted = [i for i in range(1,2001)]
with open("d_2000_sorted.txt", 'w') as txt_file:
    for value in d_2000_sorted:
        txt_file.write(str(value) + '\n')

d_2000_reversed = [2000-i for i in range(1,2001)]
with open("d_2000_reversed.txt", 'w') as txt_file:
    for value in d_2000_reversed:
        txt_file.write(str(value) + '\n')


d_20000_random = [random.randint(1, 20000) for _ in range(20000)]
with open("d_20000_random.txt", 'w') as txt_file:
    for value in d_20000_random:
        txt_file.write(str(value) + '\n')
        
d_20000_sorted = [i for i in range(1,20001)]
with open("d_20000_sorted.txt", 'w') as txt_file:
    for value in d_20000_sorted:
        txt_file.write(str(value) + '\n')

d_20000_reversed = [20000-i for i in range(1,20001)]
with open("d_20000_reversed.txt", 'w') as txt_file:
    for value in d_20000_reversed:
        txt_file.write(str(value) + '\n')


