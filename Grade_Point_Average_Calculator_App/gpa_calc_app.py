print('Welcome to the Grade Point Average Calculator App')
#Get user input
user_name = input('What is your Name: ')
num_of_grades  = int(input('How many Grades would you like to Enter: '))
grades = []
#Get the user's grades
for i in range(num_of_grades):
    grades.append(int(input('Enter Grade: ')))
#Sort the grades and print them to the screen
sorted_grades = grades.sort(reverse=True)
print(f"\nGrades Highest to Lowest:")
for grade in grades:
    print(f"{grade}")
#Calculate the average
average = lambda grade:sum(grade)/len(grade)
#Print a grade summary
print(f"{user_name.title()}'s Grade Summary:")
print(f"Total number of Grades: {len(grades)}")
print(f"Highest Grade: {max(grades)}")
print(f"Lowest Grade: {min(grades)}")
print(f"Average: {average(grades)}")
#Get the user's desired average and calculate what they need to get on the next assignment
desired_avg = float(input('What is your Desired Average: '))
grades_req = lambda x,y:x*(len(y)+1) - sum(y)
#Print a summary
print(f"Good Luck {user_name.title()}")
print(f"You will need to get a {grades_req(desired_avg,grades)} on your next assignment to earn a {desired_avg} average.")
#Make a copy of the original grades and swap out one of the grades
new_grades = grades[:]
print(f"\nLet's see what your average could have been if you did better/worse on an assignment.")
grade_change = int(input('What Grade would you like to change: '))
new_grades.remove(grade_change)
new_grade = int(input(f'What Grade would you like to change {grade_change} to: '))
new_grades.append(new_grade)
new_grades.sort(reverse=True)
print(f"\nNew Grades Highest to Lowest:")
for grade in new_grades:
    print(f"{grade}")
print(f"{user_name.title()}'s New Grade Summary:")
print(f"Total number of Grades: {len(new_grades)}")
print(f"Highest Grade: {max(new_grades)}")
print(f"Lowest Grade: {min(new_grades)}")
print(f"Average: {average(new_grades)}")
#Print a summary on how the average changed
print(f"\nYour new Average would be a {average(new_grades)} compared to your real Average of {average(grades)}")
average_change = round(average(new_grades) - average(grades),2)
print(f"\nThat is a change of {average_change}")
#Too bad the original grades are still intact!
print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit!")



