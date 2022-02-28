# Question ---> 1
# To write a recursive function to solve the problem of Tower of Hanoi
# Here, we will write the function for 3 discs
# Here, disc 1 = topmost disc ; disc 2 = middle disc ; disc 3 = last disc

def Tower_Of_Hanoi(n, source, destination, helper):
    if n == 1:
        print("Move disc 1 from source", source, "to destination", destination)
        return

    Tower_Of_Hanoi(n-1, source, helper, destination)
    print("Move disc", n, "from source", source, "to destination", destination)
    Tower_Of_Hanoi(n-1, helper, destination, source)

n = 3
Tower_Of_Hanoi(n, "A", "B", "C")



# Question ---> 2
# To write a python program to print Pascal's triangle for 'n' number of rows given by user
# We have to write the program using both recursive and iterative procedures

# Case --> 1 (Iteration)

from math import factorial
n = int(input("Enter the number : "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

# Case ---> 2 (Recursion)

def pascal_triangle(n, true_length = n):
    if n == 0:
        return
    pascal_triangle(n-1, true_length)

    print(" " * (true_length - n), end="")  # this is to print the spaces

    start = 1  # First number is always 1 in pascal triangle
    for i in range(1, n+1):
        print(start, end="  ")

        start = start * (n - i) // i  # property of binomial coefficient
    print()
pascal_triangle(n)



# Question ---> 3

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

Quotient = num1 // num2
Remainder = num1 % num2

# Part (a)
print("Checking if the quotient and remainder value is a callable value or not :")
print(callable(Quotient))  # Using callable function
print(callable(Remainder))

# Part (b)
if (Quotient == 0): # Using if-else condition
    print("The quotient is zero")
if (Remainder == 0):
    print("The remainder is zero")
if (Quotient != 0 and Remainder != 0):
    print("Yes, all the values are non zeros")

# Part (c)
add_list = [Quotient + 4, Remainder + 4, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

resultant_list = []
for i in range(len(add_list)):
    if add_list[i] > 4:
        resultant_list.append(add_list[i])
print(f"Filtered numbers that are greater than 4 are : {resultant_list}")

# Part (d)
set_datatype = set(resultant_list)  # Converting list to set datatype
print(f"The resulting set is : {set_datatype}")

# Part (e)
# To make the set immutable
immutable_set = frozenset(set_datatype)
print(f"The formed immutable set is : {immutable_set}")

# Part (f)
print(f"The maximum value of the above set is : {max(immutable_set)}")  # Finding the max value of the set
print(f"The hash value of the maximum value of the above set is : {hash(max(immutable_set))}")



# Question ---> 4
# To create a class named student and to assign values for name and roll number

class Student:
    def __init__(self, name, roll_number): # to initialise name and roll number
        self.name = name
        self.roll_number = roll_number

    def assign_values(self):
        print(self.name, self.roll_number)

    def __del__(self):  # Calling a function to delete the object
        print("The object is destroyed")

print("The object is created")
print(f"The details of the student are :")
student1 = Student("Rajat", 21103062)
student1.assign_values()

del student1  # deleting the object



# Question ---> 5
# To store details of 3 employees : name and salary using class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Creating employees' records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

# Part (a)
# To update the salary of employee1 (Mehak)
employee1.salary = 70000
print(f"The updated salary of {employee1.name} is {employee1.salary}")

# Part (b)
# To delete the record of employee3 (Viren)
print(f"The record of {employee3.name} is deleted", end="")
del employee3



# Question ---> 6
# *****  Friendship test  *****

input_word = input("Enter a word :\n")  # taking input of a word from George
input_word = input_word.lower()

# Taking input of meaningful word from the exact same letters from Barbie
test_word = input("Enter a meaningful word from the exact same letters :\n")
test_word = test_word.lower()

def count_in_dict(input_word):
    count = {}
    word_list = list(input_word)

    n = len(word_list)
    for i in range(n):
        if word_list[i] in count:
            count[word_list[i]] += 1
        else:
            count[word_list[i]] = 1
    return count

# Now, we have to take input from shopkeeper to verify the word's meaning
def shopkeeper_input():
    if count_in_dict(input_word) != count_in_dict(test_word):
        print("The letters are not the same, hence, the friendship is fake")
        return 
    answer = input("Does the word makes any sense ? (y/Y or n/N) : ")

    if answer == "y" or answer == "Y":
        print("Congratulations! Barbie and George, you passed the friendship test")
    elif answer == "n" or answer == "N":
        print("The word doesn't have any meaning. Sorry, your friendship is fake")
    else:
        print("Invalid input! Please try again")

shopkeeper_input()