import numpy as np # type: ignore

list = [1,2,3]
print(list)

arr = np.array(list)
print(arr)

print(type(arr))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

mat = np.array(matrix)
print(mat)
print(mat.ndim)
print(mat.shape)
print(mat.dtype)
print(mat.size)
print(type(mat))


# arange
arr = np.arange(10)
print(arr)

arr = np.arange(1,10)
print(arr)

arr = np.arange(1,10,2)
print(arr)

arr = np.arange(10,1,-1)
print(arr)
print()


# Reshape
arr = np.array([1,2,3,4,5,6])
newarr = arr.reshape(2,3)
print(newarr)

arr = np.array([1,2,3,4,5,6])
newarr = arr.reshape(3,2)
print(newarr)

mar = np.arange(1,10).reshape(3,3)
print(mar)

mat = np.arange(1,16).reshape(1,1,5,3)
print(mat)
print()


# linspace
arr = np.linspace(1,10,5)
print(arr)

arr = np.linspace(1,10,5,endpoint=False)
print(arr)

arr = np.linspace(1,10,5,retstep=True)
print(arr)
print()


# Random
arr = np.random.rand(5)
print(arr)

arr = np.random.rand(2,5)
print(arr)

num = np.random.randint(1,10)
print(num)

arr = np.random.randint(1,10,5)
print(arr)

# arr = np.random.randint(1,10,5, dtype=np.float64)
# print(arr)








