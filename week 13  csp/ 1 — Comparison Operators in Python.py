# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5  # True
7 == 2 * 3 + 1  # True
8 != 8  # False
4 <= 2 + 2  # True

# Write 3 examples that result in True and 3 that result in False.
10 < 11 # True
6 * 7 > 4 * 1   # True
4 == 2 * 2  # True
6 == 8  # False
5 > 7   #False
9 > 11  # False

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.
grade = int(input("Enter your score"))
if grade >= 60:
    print("You passed the test!")
else:
    print("You did not pass the test.")


# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
