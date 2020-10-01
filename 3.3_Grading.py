'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6

'''

run = True

while run:
    sem_grade = float(input("What is your semester grade? "))
    fin_grade = float(input("What is your final exam grade? "))
    fin_worth = float(input("What % is your final exam worth? "))
    sem_worth = 100 - fin_worth

    sem_grade = sem_grade * (sem_worth/100)
    fin_grade = fin_grade * (fin_worth/100)
    fin_grade = round(sem_grade + fin_grade, 1)

    print("Your final grade is: ", fin_grade, "\n")
