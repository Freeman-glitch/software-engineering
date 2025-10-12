def fix_grades(grades):
    fixed_grades = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            fixed_grades.append(4)
        else:
            fixed_grades.append(grade)
    return fixed_grades

grades_list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

result1 = fix_grades(grades_list1)
result2 = fix_grades(grades_list2)
result3 = fix_grades(grades_list3)

print(result1)
print(result2)
print(result3) 