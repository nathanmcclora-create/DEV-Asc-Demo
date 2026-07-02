def cube_number(input_number) -> int:
    cubed = input_number * input_number * input_number
    return cubed

my_start_number = 4
my_cubed_number = cube_number(my_start_number)
print(f"The cube of {my_start_number} is: {my_cubed_number}")

def greet_person(name: str) -> str:
    greeting = f"Hello, {name}!"
    return greeting

print(greet_person("Alice"))  # This will print a greeting for Alice, which is "Hello, Alice!"

my_string_example  = greet_person("Alice")
print(my_string_example)