import numpy as np 

import numpy as np 

subjects = np.array(["English","Science","Mathematics","Computer Science"])


marks = np.array([
    [88, 91, 95, 99], 
    [31, 32, 26, 22], 
    [87, 92, 94, 98],
    [56, 67, 78, 67],
    [21, 13, 15, 32]
])


students_list = np.array(["Johan" ,"Naruto","Ayanokoji","Luffy","Goku"])


percentage = marks.sum(axis=1) / 400 * 100
# print(percentage)


# avgmarks_1 = (marks[:,0].sum())/5
# avgmarks_2 = (marks[:,1].sum())/5
# avgmarks_3 = (marks[:,2].sum())/5
# avgmarks_4 = (marks[:,3].sum())/5

avg_marks = marks.sum(axis=0)/5

# print(avg_marks)



# eng_marks = marks[:,0]

# index_4 = np.argmax(eng_marks)
# print(index_4)
# print(f"The English topper is {students_list[index_4]}")

# Science_marks = marks[:,1]

# index_5 = np.argmax(Science_marks)
# print(index_5)
# print(f"The Science topper is {students_list[index_5]} ")


# Maths_marks = marks[:,2]

# index_6 = np.argmax(Maths_marks)
# print(index_6)
# print(f"The Mathematics topper is {students_list[index_6]} ")

# Cs_marks = marks[:,3]

# index_7 = np.argmax(Cs_marks)
# print(index_7)
# print(f"The Computer Science topper is {students_list[index_7]} ")


sub_avg_marks = np.argmax(marks,axis=0)

# for i,mark in enumerate(sub_avg_marks) :
#     print(print(f"The {subjects[i]} topper is {students_list[mark]}"))

for i in sub_avg_marks :
    print(i)