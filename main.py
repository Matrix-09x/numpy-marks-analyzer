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

condition = ( (percentage >= 90) ,
             (percentage >= 80)  & (percentage < 90) ,
             (percentage >= 70) & (percentage < 80),
             (percentage >= 60) & (percentage < 70),
             (percentage >= 50) & (percentage < 60),
             (percentage >= 40) & (percentage < 50),
             (percentage >= 33) & (percentage < 40),
             (percentage < 33)

)

grades = ("A1","A2","B1","B2","C1","C2","D","E")

grades_student = np.select(condition,grades,percentage)

# print(grades_student)

for i,student  in enumerate(percentage) :
    print(f"{students_list[i]} percentage - {percentage[i]} , Grade - {grades_student[i]}")






index = np.argmax(percentage)
index_1 = np.argmin(percentage)

print(f"Topper : {students_list[index]}")
print(f"Lowest Scoring Student : {students_list[index_1]}")

failed_students =  np.where(percentage < 33)[0]

# print(failed_students)
failed_students_count = len(failed_students)
print(f"Total failed students : {failed_students_count}")

failed_names = students_list[failed_students]
names = ",".join(failed_names)
# print(names)
print(f"Failed students : {names}")



Distinction_students =  np.where(percentage  > 75)[0]

# print(Distinction_students)
Distinction_students_count = len(Distinction_students)
print(f"Total  Distinciton stidents  : {Distinction_students_count}")

Distinction_names = students_list[Distinction_students]
names_2 = ",".join(Distinction_names)
# print(names)
print(f"Distinction students : {names_2}")






avg_marks = marks.mean(axis=0)

for i,avg  in enumerate(avg_marks) :
    print(f"The average marks of {subjects[i]} is {avg}")



index_2 = np.argmax(avg_marks)
index_3 = np.argmin(avg_marks)

print(f"The subject with highest avg : {subjects[index_2]}")
print(f"The subject with lowest avg : {subjects[index_3]}")
print(f"Hardest subject : {subjects[index_3]}")
print(f"Easiest subject : {subjects[index_2]}")


sub_avg_marks = np.argmax(marks,axis=0)

# print(sub_avg_marks)

for i,mark in enumerate(sub_avg_marks) :
    print(f"The {subjects[i]} topper is {students_list[mark]}")


sorted_array = np.argsort(percentage)[::-1]




ranked_students = students_list[sorted_array]



ranked_list = []

for i, rank in enumerate(ranked_students,1) :
    
    ranked_list.append(f"{i}.{rank}")
    

# print(ranked_list)

clean_names = " ".join(ranked_list)
print(f"Ranks : {clean_names}")















