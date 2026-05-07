# program to calculate salary of an official based on the no of leaves taken by them

leaves = int(input("Enter the number of leaves taken: "))
BP = int(input("Enter the basic pay: "))
OA = 10000 #Other Allowance

if(leaves < 5):
    sal= BP + OA

elif(leaves >= 5 and leaves < 20):
    sal = (BP/2) + OA

else:
    sal = 0

print("The salary of the official for the month is: ", sal)

#End of program