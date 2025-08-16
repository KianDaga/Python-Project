students_score = {
  "Thomas" : 57,
  "James": 80,
  "Jane": 95,
  "Lucas": 65
}

# Do not change the code above ☝️
#################################################################

# TODO 1: Create an empty dictionary, students_grade

# TODO 2: Add each student name from students_score dictionary as the key 
#         and the value is the grade of the student

student_grades = {
    
}

for key in students_score:
    score = students_score[key]
    if score >= 80:
        grade = "A"
    elif 60 <= score <= 79:
        grade = "B"
    elif 55 <= score <= 59:
        grade  = "C"
    elif 50 <= score <= 54:
        grade = "D"
    else:
        grade = "F"       

    student_grades[key] = grade
#################################################################
# Do not change the code below 
print(student_grades)




