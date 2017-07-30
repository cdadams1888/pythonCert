# 1. Write a program which prints hello world
print("hello world")

# 2. Write a program which should use following operators
number1 = 2
number2 = 5

# a. Addition
added = number1 + number2
print(added)

# b. Subtraction
subtracted = number1 - number2
print(subtracted)

# c. Multiplication
multiplied = number1 * number2
print(multiplied)

# d. Division
divided = number1 / number2
print(divided)

# 4. Write a program using while loop
while number1 < number2:
    number1 += 1
    print("number1 is still less than number2.")

# 5. Write a program using if else statement
if number1 < number2:
    print("number1 is less than number2")
else:
    print("number1 is greater than number2")

# 6. Perform following operations on List:
myList = [1,5,6,8,9, "Christopher", "Adams"]

# a. Concatenation
fullName = myList[5] + " " + myList[6]
print("My full name is",fullName)

# c. Updation
myList[5] = "Dewy"
print(myList[5])

# d. Deletion
myList.remove(5)

# 7. Write a program to print the current month calendar
import datetime
now = datetime.datetime.now()
print "Current month: %d" % now.month

# 8. Write a program of file handling using following methods:
import os

# a. rename()
os.rename('testDirectory', "newTestDirectory")

# b. remove()
os.remove('testFile.py')

# c. mkdir()
os.mkdir('testDirectory1')

# d. rmdir()
os.rmdir('testDirectory1')

# e. getcwd()
os.getcwd()

# 9. Write a program by using match function

# 10. Write a program using class concept.
class Animal:
    def __init__(self, color):
        self.color = color
