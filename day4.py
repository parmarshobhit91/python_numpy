import numpy as np  

# Log example
arr = np.log2(10)
print(arr)

arr = np.log10(100)
print(arr)

arr = np.log(9)
print(arr)

# Exponential example
arr_exp = np.exp(2)
print(arr_exp)

arr_exp_base3 = np.exp2(3)
print(arr_exp_base3)

arr = np.array([1, 2, 3, 4, 5])
arr_exp_elements = np.exp(arr)
print(arr_exp_elements)

new_arr = np.arange(1, 10, 1).reshape(3, 3)
print(new_arr)

arr_flatten = new_arr.flatten()
print("Flattened Array:", arr_flatten)

arr_eye = np.eye(3,3)
print("Identity Matrix (4x4):\n", arr_eye)

arr_empty = np.empty((2,3))
print("Empty Array (2x3):\n", arr_empty)

arr_full = np.full((2,3), 7)
print("Full Array (2x3) with 7s:\n", arr_full)

# Transpose example
arr_transpose = np.array([[1, 2, 3], [4, 5, 6]])
transposed_arr = arr_transpose.T
print("Transposed Array:\n", transposed_arr)

arr_2_transpose = np.array([[7, 8], [9, 10], [11, 12]])
new_transposed_arr = np.transpose(arr_2_transpose)
print("New Transposed Array:\n", new_transposed_arr)    

# Concatenate example
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("Concatenated Array along axis 0:\n", concatenated_arr)


concatenated_arr = np.concatenate((arr1, arr2), axis=1)
print("Concatenated Array along axis 0:\n", concatenated_arr)

arr3 = np.array([[13, 14, 15], [16, 17, 18]])
arr4 = np.array([[19, 20, 21], [22, 23, 24]])

new_concat_arr = np.vstack((arr3, arr4))
print("Vertically Stacked Array:\n", new_concat_arr)

new_concat_arr = np.hstack((arr3, arr4))
print("Horizontally Stacked Array:\n", new_concat_arr)