import numpy as np 

array_0 = np.array('a')


array_1 = np.array([1,2,3])

array_2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]
                  ])

# print(array_2[1,0])   


# 3d array

array_3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                  [[10,11,12],[13,14,15],[16,17,18]],
                  [[19,20,21],[22,23,24],[25,26,27]],
                  ])                
# print(f"{array[1,2,1]}/{array[1,0,0]}/{array[2,0,1]}{array[1,0,0]}")  # multidimensional indexing to get values and to make it a D.O.B 

# slicing

array_4 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]
                  ])

# print(array.flatten()[4:11])



# Scalor Arithmetic 

radii =  np.array([1,2,3,4]) # radius of a spheres

# print(4 * np.pi * radii ** 2)   # surface area of each speher



# element wise arithmetic

array_5 =  np.array([1,2,3,4])
array_6 =  np.array([5,6,7,8,])
# print(array_5 * array_6)


# comparison operators

scores = np.array([
    [78, 92, 65],
    [84, 55, 90],
    [99, 73, 81]
])

# scores = scores[scores % 2 == 0 ]
 
# Broadcasting


array_8 = np.array([[1,2,3,4,5]])

