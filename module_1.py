grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_of_students=sorted(students)
average_grades = {}
for student_name, grade_average in zip(sort_of_students, grades):
    average_grade = sum(grade_average) / len(grade_average)
    average_grades[student_name] = average_grade
print(average_grades)