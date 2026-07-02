# # # if , elif, else

# # # my_favorite_cars  = 
# [
#     {
# # #     "car_name": "Tesla",
#     # # "model": "Model S",
#     # # "year": 2020, # Number(int)
#     # # "price": 79999.99, # Number(float)
#     # # "features": ["Autopilot", "Electric", "Luxury", "All-Wheel Drive"], # List
#     # # "is-available": True, # Boolean
#     # # "owner": None, # None
#     },
#     {   
#     # # "car_name": "Porsche",
#     # # "model": "911 Carrera",
#     # # "year": 2021,
#     # # "price": 120000.00,
#     # # "features": ["Sports", "Luxury", "Rear-Wheel Drive", "Turebocharged"],
#     # # "is-available": False,
#     # # "owner": None
#     };
# ]


# # if my_favorite_cars == []:
# #     print("This list is empty")
# #     print("Please add some cars to the list.")
# #     print("Thank You!")

# # elif my_favorite_cars[0]["is-available"]:
# #     print("This list is NOT empty")
# #     print(my_favorite_cars[0]["car_name"], "is available for purchase.")

# # else:
# #     print("This list is NOT empty")
# #     print(my_favorite_cars[1]["car_name"], "is NOT available for purchase.")


# # n = 1000

# # if n < 50:
# #     print("n is less than 50")
    
# # elif n == 1000:
# #     print("n is equal to 1000")

# # else:
# #     print("The number is greater than 1000")




# # MATCHES NOTES: We will illustrate how to handle various HTTP status codes, including 200, 301, 401, 403, and 404, using match.
# #  We will also show how to use comments to temporarily disable code blocks, allowing us to focus on the relevant parts of our script. 
# # By the end, we will have a cleaner approach to managing complex branching logic without relying on multiple if-else statements.


# # HTTP Request Codes: 200: ok; 201: SUBMITTED & UPDATED, 202: aCCCPETED, NOT UPDATED YET
# # 301: moved permanently; 
# # 401: unauthorized; 403: forbidden; 404: not found;

# code = 404 # You can change this value to test different cases
# # code = 301
# # code = 200


# match code:
#     case 200:
#         print("OK: The request has succeeded.")
#     case 201:
#         print("Created: The request has been fulfilled and resulted in a new resource being created.")
#     case 202:
#         print("Accepted: The request has been accepted for processing, but the processing has not been completed.")
#     case 301:
#         print("Moved Permanently: The requested resource has been assigned a new permanent URI.")
#     case 401:
#         print("Unauthorized: The request requires user authentication.")
# #     case 403:
# #         print("Forbidden: The server understood the request, but refuses to authorize it.")
#     case 404:
#         print("Not Found: The server has not found anything matching the Request-URI.")
#     case _:
#         print("Unknown status code.")       

#  =================================================


#  FOR Examples in Python, we can use the "for" loop to iterate over a sequence (like a list, tuple, or string) and execute a block of code 
# for each item in that sequence. Here's an example of how to use a for loop in Python:

fruits = ["apple", "banana", "cherry"]

# my_favorite_cars  = [
#     {
#         "car_name": "Tesla",
#         "model": "Model S",
#         "year": 2020, # Number(int)
#         "price": 79999.99, # Number(float)
#         "features": ["Autopilot", "Electric", "Luxury", "All-Wheel Drive"], # List
#         "is-available": True, # Boolean
#         "owner": None, # None
#     },
#     {   
#         "car_name": "Porsche",
#         "model": "911 Carrera",
#         "year": 2021,
#         "price": 120000.00,
#         "features": ["Sports", "Luxury", "Rear-Wheel Drive", "Turebocharged"],
#         "is-available": False,
#         "owner": None
#     },

#     {
#         "car_name": "BMW",
#         "model": "3 Series",
#         "year": 2022,
#         "price": 45000.00,
#         "features": ["Luxury", "Sports", "All-Wheel Drive"],
#         "is-available": True,
#         "owner": None
#     },
#     {
#         "car_name": "Audi",
#         "model": "A4",
#         "year": 2021,
#         "price": 40000.00,
#         "features": ["Luxury", "All-Wheel Drive"],
#         "is-available": True,
#         "owner": None
#     }
# ]

# for car in my_favorite_cars:
#     print(car)
#     print("next item:")



# for car in my_favorite_cars:
#     if car['car_name'] == 'Tesla':
#         print("The first item is a Tesla car.")
#         print(car["car_name"], "-", car["model"], "-", car["year"])
#     else:
#         print("The first item is NOT a Tesla car.")
#         print(car["car_name"], "-", car["model"], "-", car["year"])

# if any(car['car_name'] == 'Porsche' for car in my_favorite_cars):
#     print("There is a Porsche car in the list.")
# else:
#     print("There is NO Porsche car in the list.")


    # print(car["car_name"], "-", car["model"], "-", car["year"])
    # print(car["car_name"], "-", car["model"], "-", car["year"])
    # print("next item:")

    # BREAK EXAMPLE: The break statement is used to exit a loop prematurely when a certain condition is met.

# for car in my_favorite_cars:
#     if car['car_name'] == 'BMW':
#         print("The first item is a BMW car.")
#         print(car["car_name"], "-", car["model"], "-", car["year"])
#         break  # Exit the loop after finding the first BMW car
#     else:
#         continue  # Continue to the next iteration if the car is not a BMW


#  =================================================

# TRY . . . .EXCEPT: The try-except block is used to handle exceptions (errors) that may occur during the execution of a program.

my_favorite_cars  = [
    {
        "car_name": "Tesla",
        "model": "Model S",
        "year": 2020, # Number(int)
        "price": 79999.99, # Number(float)
        "features": ["Autopilot", "Electric", "Luxury", "All-Wheel Drive"], # List
        "is-available": True, # Boolean
        "owner": None, # None
    },
    {   
        "car_name": "Porsche",
        "model": "911 Carrera",
        "year": 2021,
        "price": 120000.00,
        "features": ["Sports", "Luxury", "Rear-Wheel Drive", "Turebocharged"],
        "is-available": False,
        "owner": None
    },

    {
        "car_name": "BMW",
        "model": "3 Series",
        "year": 2022,
        "price": 45000.00,
        "features": ["Luxury", "Sports", "All-Wheel Drive"],
        "is-available": True,
        "owner": None
    },
    {
        "car_name": "Audi",
        "model": "A4",
        "year": 2021,
        "price": 40000.00,
        "features": ["Luxury", "All-Wheel Drive"],
        "is-available": True,
        "owner": None
    },
    {
        "model": "Civic",
        "year": 2020,
        "price": 22000.00,
        "features": ["Compact", "Fuel Efficient", "Front-Wheel Drive"],
        "is-available": True,
        "owner": None
    },
    {
        "car_name": "Ford",
        "model": "Mustang",
        "year": 2021,
        "price": 35000.00,
        "features": ["Sports", "Rear-Wheel Drive"],
        "is-available": False,
        "owner": None
    }
]

# my_favorite_cars[0]["car_name"] = None
# for car in my_favorite_cars:
#     try:
#         if car["car_name"] is None:
#             raise ValueError("Car name is missing.")
#         print(car["car_name"], "-", car["model"], "-", car["year"])
#     except KeyError as e:
#         print(f"KeyError: {e} is missing in the car dictionary.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# my_favorite_cars[0]["car_name"] = "Tesla"
# for car in my_favorite_cars:
#     try:
    #     if car["car_name"] == "Tesla":
    #         print("The first item is a Tesla car.")
    #         print(car["car_name"], "-", car["model"], "-", car["year"])
    #         break  # Exit the loop after finding the first Tesla car
    #     else:
    #         continue  # Continue to the next iteration if the car is not a Tesla
    # except KeyError as e:
    #     print(f"KeyError: {e} is missing in the car dictionary.")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")

# ANOTHER EXAMPLE: Using try-except to handle potential KeyError when accessing the "car_name" key in the car dictionary:

    #     if car["car_name"] == "Tesla":
    #         print("Tesla car found in the list.")
    #         print(car["car_name"], "-", car["model"], "-", car["year"])
    #         break  # Exit the loop after finding the first Tesla car
    #     else:
    #         print("No Tesla car found in the list.")
    #         continue  # Continue to the next iteration if the car is not a Tesla
    # except KeyError as e:
    #     print(f"KeyError: {e} is missing in the car dictionary.")
    # finally:
    #     print("Finished checking the car list.")    


# CHALLENGE: Write a Python program that iterates through the my_favorite_cars list and prints the car price is greater than 100000. 
# If the car price is less than or equal to 50000, it should print that the car is affordable. 
# Use try-except to handle any potential KeyError when accessing the "price" key in the car dictionary.

for car in my_favorite_cars:
    try:
        if car["price"] > 100000:
            print(f"{car['car_name']} - {car['model']} is expensive with a price of ${car['price']}.")
        # elif car["price"] <= 50000:
        #     print(f"{car['car_name']} - {car['model']} is affordable with a price of ${car['price']}.")
        # else:
        #     print(f"{car['car_name']} - {car['model']} has a moderate price of ${car['price']}.")
    except KeyError as e:
        print(f"KeyError: {e} is missing in the car dictionary.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # DONE