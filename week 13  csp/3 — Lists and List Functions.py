# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# collections are used to store multiple items in a single variable
# lists are ordered collections of items
# lists are mutable, meaning you can change their content
# lists are created using sqaure brackets
list_of_fruits = ['apple', 'banana', 'cherry', 'date']
print(list_of_fruits) # ["apple", "banana", "cherry", "date"]
print(type(list_of_fruits)) # <class 'list'>
# Accesing items in a list
print(list_of_fruits[0]) # apple
print(list_of_fruits[1]) # banana
print(list_of_fruits[-1]) # date
print(list_of_fruits[1:3]) # ['banana, 'cherry']
# reversing a list 2 ways
list_of_fruits.reverse()
print(list_of_fruits) # ["date", "cherry", "banana", "apple"]
print(list_of_fruits[::-1]) # ["apple", "banana", "cherry", "date"]
# Appending items to a list
list_of_fruits.append("elderberry") # add items to the end of the list
print(list_of_fruits)
list_of_fruits.append("kiwi")
list_of_fruits.append("mango")
print(list_of_fruits)
list_of_fruits.extend(["fig", "grape", "honeydew"])
# add multiple items to the end of the list
print(list_of_fruits)
list_of_fruits.reverse()
print(list_of_fruits)
# popping items from a list
popped_item = list_of_fruits.pop()
# removes and returns the last item
print(popped_item) # honeydew
print(list_of_fruits)
# insert items at a specific index
list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)
# removing a specific item value
list_of_fruits.remove("banana")
print(list_of_fruits)
# index 3
list_of_fruits.insert(3, "watermelon")
print(list_of_fruits)
list_of_fruits.sort() # sorts the list in ascending order
print(list_of_fruits)
# Why use lists instead of variables
# imagine you have 100 items to manage
list_of_items = list(range(1,101))
print(list_of_items)
list_of_items = list(range(1,1001))
print(list_of_items)
print(len(list_of_items)) # 1000
# extend by a 1000 more items
list_of_items.extend(range(1001, 2001))
print(len(list_of_items)) # 2000

# why use lists
# instead of creating seperate variables
# for each item, we can store them in a list
# this makes our job easier
# this makes managing the complexity of our code easier
# when we need to managa multiple items
# performance task answer


# sets and tuples
# sets and tuples are also part of the collections family in python
# sets examples
set1 = {1, 2, 3, 4, 5}
set2 = {"apple,", "banana", "cherry"}
print(set1)
print(set2)
print(type(set1))
# why use sets instead of lists?
# sets automatically handle duplicate items
# examples:
set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(set_with_duplicates)
# sets are useful for membership testing
print(3 in set1) # True
print(6 in set1) # False
# tuples examples:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apple", "banana", "cherry")
print(tuple1) # (1, 2, 3, 4, 5)
print(tuple2) # ("apple", "banana", "cherry")
print(type(tuple1)) # <class 'tuple'>
# why use tuples instead of lists?
# tuples are immutable, meaning they cannnot be changed after creation
# this makes tuples usefel for storing data that should not be modified
# exmaples:
social_security_number = (123444, 4444445, 5676789)




# # Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
list_fav_food = ('burger', 'pizza', 'fries', 'water', 'watermelon')
# Print the second and last item.
print()
# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.