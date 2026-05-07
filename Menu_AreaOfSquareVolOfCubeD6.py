# program to display a menu and calculate the area of a square and volume of a cube

print(" 1. Calculate the area of a square")
print(" 2. Calculate the volume of a cube")
choice = int(input("Enter your choice: "))
side = int(input("Enter the side length: "))

if choice == 1:
    print("The Area of the square is: ", side * side) #Area of the square is calculated and displayed
else:
    print("The Volume of the cube is: ", side * side * side) #Volume of the cube is calculated and displayed

    # End of program

