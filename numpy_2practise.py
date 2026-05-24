import numpy as np 
 

# Broadcasting

array = np.array([[1,2,3],
                  [4,5,6]])
array_2 = np.array([[[1,2,3],
                     [2,3,5],
                     ]
                    ])
                    
# print(np.shape(array))
# print(np.shape(array_2))
# print(array * array_2)
# print(array + array_2)
# print(array - array_2)
# print(array / array_2)
                     
                    
                    
                     
                     





scores = np.array([
        [70, 80, 90],
        [60, 75, 85],
        [88, 92, 77]
    ])

conditions = [ (scores <= 70) ,
                (scores > 70)  & (scores <= 85) ,
                (scores> 85)
    ]

check = ["Average","Good","Excellent"]

final= np.select(conditions,check,default= "below average")
print(final)


# aggreagate functions


array_3  = np.array([[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
],
[
    [13,14,15,16],
    [17,18,19,20], 
    [21,22,23,24]
]

])




# print(np.sum(array_3,axis=0))
# print(np.sum(array_3,axis=1))
# print(np.sum(array_3,axis=2))


# scores_1 = np.array([
#     [72, 85, 90],
#     [60, 78, 88],
#     [95, 91, 89]
# ])


# print(np.mean(scores_1))
# print(np.std(scores_1))
# print(np.var(scores_1))



#filtering 


scores_2 = np.array([
    [72, 85, 91],
    [60, 78, 88],
    [95, 91, 89],
    [45, 67, 70]
])


condition = (
    (scores_2 >=  90),
    (scores_2 >= 70) & (scores_2 < 90) ,
    (scores_2 < 70)
)

check = ("Excellent" , "Good" , "Needs Improvemt")

result = np.select(condition,check,scores_2)

masks = scores_2[scores_2  > 80]
# print(masks)


# random number 


rng = np.random.default_rng(3)

# print(rng.integers(1,101,(3,2)))


array_8 = np.array([1,2,3,4,5,6,7])
# rng.shuffle(array_8)
yo = rng.choice(array_8)
# print(yo)
# for float 

np.random.seed(1)

# print(np.random.uniform(1,2,[2,3]))




#reshaping 
yoyo_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

yoyo_array = yoyo_array.reshape(2,2,-1)

# print(yoyo_array)


# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9],
#                 [10,11,12],
#                ])
                
# arr = arr.reshape(2,2,3)
# print(arr)
               
               
# Transpone

# arr = np.array([
    
#     [
#         [1,2,3,4],
#         [4,5,6,4],
#         [4,5,6,4]
#     ],
    
#     [
#         [7,8,9,4],
#         [10,11,12,3],
#         [10,11,12,5]
#     ]
    
# ])

# print(arr.shape)      
# print(arr.T.shape)



arr = np.array([[1,2,3,7],
                [4,5,6,9],
               ])


arr_2 = np.array([[5,6,7],
                  [8,9,10],
                  [11,12,13],
                  [14,15,16],
               ])
                  
print(np.dot(arr,arr_2))
  

  