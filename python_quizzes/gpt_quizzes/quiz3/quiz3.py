"""Arguments"""
# 1. Write a function named decrive_city that takes two positional arguements

def describe_city(city_name, country):
    return (f"{city_name} is in {country}.")

fact = describe_city("Paris", "France")

# 2. Default Arguements, Create a function named greet_user that: 
# Accepts two arguements: name and greeting
# The greeting argument should havea  default value of "Hello".
# Call it with and without the second argument

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}"

first = greet_user("Kimberly", "I love you")
second = greet_user("Kimberly")

print(first)
print(second)

# 3. Arbitrary positional arguements

def list_fruits(*fruits):
    return [fruit for fruit in fruits]

list_fruits("Apple", "Banana", "Cherry")

# 4. Arbitrary Keword Arguments

def build_profile(first_name, last_name, **kwargs):
    return {'first_name': {first_name}, 'last_name': {last_name}, **kwargs}

profile = build_profile("Alice", "Smith", age=30, location="New York")

print(f"{profile}\n")

# 5. All argument types together

def order_food(main_dish, drink='water', *sides, **special_requests):
    # Convert sides tuple to comma-separated string
    sides_str = ", ".join(sides)

    # Convert special requests dict to comma-separated string
    requests_str = ", ".join(f"{value}" for value in special_requests.values())
    return f"Main: {main_dish}\nDrink: {drink}\nSides: {sides_str}\nSpecial Request: {requests_str}"

order = order_food("Spicy Chicken Sandwich", "powerade", "honey mustard", "buffalo sauce",
           special_requests1='no tomato', special_requests2='sauce o/s')
print(order)


# def build_profile1(first_name, last_name, **kwargs):
#     user_profile = {'first_name': {first_name}, 'last_name': {last_name}, **kwargs}
#     for key, value in user_profile.items():
#         print(f"{key}: {value}")
#     return user_profile
# profile1 = build_profile1("Kimberly", "Banuelos", age=31, location="Los Angeles")
# print(profile1)