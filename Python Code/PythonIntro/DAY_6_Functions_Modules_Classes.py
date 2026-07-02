print([1,2,3], "Hello World", 3.147458751, True, None, {1,2,3}, (1,2,3), [1,2,3], {"a":1, "b":2, "c":3}, {"name":"John", "age":30})

my_string ="My favorite number is:"
my_number = 71717

print(my_string, my_number)

# Example of making my_number a string using str() function
print(my_string + " " + str(my_number))

# Example of making my_string a number using int() function
print(my_string + " " + str(int(my_number)))


my_string_number = "100"
print(int(my_string_number) + my_number) # This will convert the string "100" to an integer and add my_number to it, resulting in 71817

# Solution:
# My favorite number is: 71717
# My favorite number is: 71717
# My favorite number is: 71717
# 71817

my_unsorted_list = [5, 2, 9, 1, 5, 6]
# Sorting the list in ascending order
my_sorted_list = sorted(my_unsorted_list)
print(my_sorted_list)

# Solution:
# [1, 2, 5, 5, 6, 9]