import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print("Array:", arr)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("2D Array:\n", arr2)

# arr3 = np.array([[[1], [2]], [[3], [4]]])
# print("3D Array:\n", arr3)

# Multiplication of two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a * b
print("Element-wise multiplication:", result)

# Sum of two arrays
sum_result = a + b
print("Element-wise sum:", sum_result)

# Difference of two arrays
diff_result = b - a
print("Element-wise difference:", diff_result)

# Division of two arrays
div_result = b / a
print("Element-wise division:", div_result)

# Shape of an array
shape = a.shape
print("Shape of a:", shape)
print("Shape of arr2:", arr2.shape)


# Dimensions of an array
dimensions = a.ndim
print("Dimensions of arr3:", dimensions)
dimensions_arr2 = arr2.ndim
print("Dimensions of arr2:", dimensions_arr2)

# Size of an array
size = a.size
print("Size of arr:", size)
print("Size of arr2:", arr2.size)

zeros_arr = np.zeros((1,3), dtype=int)
print("New array of zeros:", zeros_arr)
print("Data type of zeros_arr:", zeros_arr.dtype)

ones_arr = np.ones((2,2))
print("New array of ones:\n", ones_arr)

