import numpy as np

# Creating a 1D array of integers from 1 to 10
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr = np.arange(0, 10, 2) 
# print("Array:", arr)

arr2 = np.array([12, 14, 16, 18, 20])
# print("Array 2:", arr2[::2])


# Creating a 2D array (3x3 matrix)
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing the 2D array to skip every second column
# print(arr3[:, ::2])

arr4 = np.array([10, 20, 30, 40, 50])
# Adding 5 to each element
arr4 += 5
print("After adding 5:", arr4)

# linespace example