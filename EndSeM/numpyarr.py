import numpy as np

#create 1-D array from range 13-39.
arr = np.arange(13,40)
#reshape this array to 9x3
arr = arr.reshape(9,3)
#split into 3 equal-size sub-arrays
arr = np.array_split(arr, 3)

print(arr)