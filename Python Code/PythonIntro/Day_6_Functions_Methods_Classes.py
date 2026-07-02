# # Built-in functions - - - first video in class


# # len() - returns the length of an object
# # print() - prints the specified message to the screen
# # input() - allows user input
# # sorted() - returns a sorted list of the specified iterable

# # print([1,2,3, "Hello", 3.1478458, True, False, None, [1,2,3], {1,2,3}, (1,2,3), {"a": 1, "b": 2, "c": 3}]) # prints the list

# #  SOLUTION: 1. Create a list with different data types and print it using the print() function.
# # [1, 2, 3, 'Hello', 3.1478458, True, False, None, [1, 2, 3], {1, 2, 3}, (1, 2, 3), {'a': 1, 'b': 2, 'c': 3}]


# my_string = "My favorite number is:"
# my_number = 71
# print(my_string, my_number) # prints the string and number

# # Solution: 2. Create a string and a number variable and print them using the print() function.
# # My favorite number is: 71


# #  or you can change the data type of the number to string and concatenate it with the string.

# print(my_string + " " + str(my_number)) # prints the string and number

# # Solution: 3. Create a string and a number variable and print them using the print() function by changing the data type of the number to string and concatenating it with the string.
# # My favorite number is: 71

# # Can convert my_string into an integer

# my_string_number = "784"
# print(my_string_number + str(my_number))  # prints the string as an integer

# # solution: 4. Create a string variable that contains a number and a number variable. 
# # Print them using the print() function by changing the data type of the string to an integer and adding it to the number variable.

# # 78471

# print(my_string + " " + str(int(my_string_number) + my_number))  # prints the string as an integer

# # Solution: 5. Create a string variable that contains a number and a number variable.
# # My favorite number is: 855

# # Example of using len() function to get the length of a string

# print(len([1,2,3, "Hello", 3.1478458, True, False, None, [1,2,3], {1,2,3}, (1,2,3), {"a": 1, "b": 2, "c": 3}])) # prints the length of the list

# # solution: 6. Create a list with different data types and print the length of the list using the len() function.
# # 12

# # Examples of sorted() function 

# my_unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(sorted(my_unsorted_list))  # prints the sorted list

# # Solution: 7. Create a list of numbers and print the sorted list using the sorted() function.
# # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# =======================================================================


cubeNumber = 3
cube = cubeNumber ** 3

print("The cube of", cubeNumber, "is", cube)  # prints the cube of the number


greetPerson = "Hello, " + "John" + "!"
print(greetPerson)  # prints the greeting message


