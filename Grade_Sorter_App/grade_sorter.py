print('-' * 35)
print('Welcome to the Grade Sorter App'.center(35))
print('-' * 35)
#Initialize list and get user input
grades_list = []
num_grades = int(input('Enter no of Grades you want Add: '))
for grade in range(0, num_grades):
    print('Enter your Grade',grade,':')
    grades = int(input())
    grades_list.append(grades)
print(f'Your Grades are: {grades_list}')
#Sort the list from highest to lowest
grades_list.sort(reverse=True)
print(f'Your Grades from Highest to Lowest are: {grades_list}')
#Removing the lowest two grades.
drop_item = 0
while drop_item != 2:
    removed_grade = grades_list.pop()
    drop_item += 1
    print(f'Removed grades: {removed_grade}')
#Recap remaining grades
print(f'Your reamining Grades are:{grades_list}')
print(f'Nice Work! Your Highest Grade is {grades_list[0]}')