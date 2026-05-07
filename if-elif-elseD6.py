#Program to check the working of if-elif-else statement

marks = int(input("Enter the marks: "))

if(marks >= 75):
    print("Student got DISTINCTION")
elif(marks < 75 and marks >=50):
    print("Student is PASS")
else:
    print("Student is FAIL")

# End of program