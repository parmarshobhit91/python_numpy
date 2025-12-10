import numpy as np

# linspace example
arr_linspace = np.linspace(1, 5, 5)  # 5 evenly spaced numbers between 0 and 1
print("Linspace Array:", arr_linspace)

# logspace example
arr_logspace = np.logspace(1, 3, 3)  # 3 numbers between 10^1 and 10^3
print("Logspace Array:", arr_logspace)

arr_logspace_base2 = np.logspace(1, 3, 3, base=2)  # 3 numbers between 2^1 and 2^3
print("Logspace Array with base 2:", arr_logspace_base2)

# arange example
arr_arange = np.arange(10, 100, 10)  
print("Arange Array:", arr_arange)

new_reshaped_arr = arr_arange.reshape(3,3)
print("Reshaped Array (3x3):\n", new_reshaped_arr)

# Random number generation
random_arr = np.random.rand(4,4) # 4x4 array of random numbers between 0 and 1
print("Random Array:\n", random_arr)

random_num = np.random.randint(1, 100)  # Random integer between 1 and 100
print("Random Integer:", random_num)

# Create a 3x3 array of random integers between 1 and 50
random_int_arr = np.random.randint(1, 50, size=(3,3))
print("3x3 Array of Random Integers:\n", random_int_arr)

r = np.random.randint(1, 100, (3,3))
print(r)