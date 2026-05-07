# Program to grade allocation based on marks

marks = int(input("Enter the marks: "))

if(marks >= 90):
    print("Grade: A")
elif(marks < 90 and marks >= 75):
    print("Grade: B")
elif(marks < 75 and marks >= 60):
    print("Grade: C")
elif(marks < 60 and marks >= 50):
    print("Grade: D")
else:
    print("Fail")

#End of program