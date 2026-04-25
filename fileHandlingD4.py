# Writing to a file
file = open("example.txt", "w")
file.write("Hello, this is a file. \n")
file.write("Python makes file handling easy. \n")
file.close()

# Reading from a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()