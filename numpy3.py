import numpy as np

array = np.array([
    [1,2,3],
    [4,5,6]
    
])

arr = np.array([
    [6,7,8],
    [9,10,11]
])

result = np.stack((array,arr))

print(result)

print(result.shape)
# array = np.array([1,2,3])

# arr = np.array([6,7,8])
# print(result)