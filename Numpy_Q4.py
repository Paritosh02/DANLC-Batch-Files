import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6],[1, 2, 3])

np_list = np.array(my_list)
np_tuple = np.array(my_tuple)

print("List to array : ", np_list)
print("Tuple to array : \n", np_tuple)
