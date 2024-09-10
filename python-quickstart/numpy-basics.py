import numpy as np


# create a "vector"
v = np.array([1, 3, 6])
print(v)

# multiply a "vector"
print(2*v)


# create a matrix
X = np.array([v, 2*v, v/2])
print(X)

# matrix multiplication
print(np.matmul(X,v))


# create a 1D array with 3 equally spaced values between 1 and 9
z = np.linspace(1, 9, 3)
print(z)


# adding and substracting arrays
print(v + z)
print(v - z)


# reshaping arrays
print(X.reshape((9,)))
print(X.flatten())


# dot product
print(np.dot(v, z))
# cross product
print(np.cross(v, z))


# mean
print(np.mean(v))
# min
print(np.min(v))
# max
print(np.max(v))


# array of random numbers between 0 and 1
print(np.random.rand(2,2))
# array of random ints between 0 and 10
print(np.random.randint(0, 10, size=5))