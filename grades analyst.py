#in this code im going to creat a program that can analyse students grades

grades = [7.5, 5.0, 10.0, 4.5, 8.0] #list with all the grades from the class
for grade in grades:
    if grade >= 7.0: # if the grade is greather or equal to 7.0 it should print approved
        print(f'Grade {grade}: Approved!')
    else: #if it is something diferent than that  it gonna print failed
        print(f'Grade {grade}: Failed!')

print(f'average grade: {sum(grades) / 5}') # this line make the average grade from the class
#the print gonna be 7.0