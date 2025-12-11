import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = a[a > 25]
print(b)
# Output: [30 40 50]

c = np.where(a > 25, a, -1)
print(c)
# Output: [-1 -1 30 40 50]

d = np.where(a > 25, a, 0)
print(d)
# Output: [ 0  0 30 40 50]

# np.min
# np.max
# np.mean
# np.median
# np.std
# np.var