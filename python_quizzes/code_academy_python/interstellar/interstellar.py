# Starting variables
earth_weight = 185

# Dictionary for planets and their relative gravity
planet_gravity = {
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19
}

# General information
print("I have information for the following planets:\n")
print("1. Venus   2. Mars    3. Jupiter\n4. Saturn  5. Uranus   6. Neptune\n")

# Function to calculate weight on a new planet
def new_planet_weight(earth_weight, planet_name):
    if planet_name in planet_gravity:
        new_weight = earth_weight * planet_gravity[planet_name]
        print(f"Your weight on {planet_name} would be: {new_weight} lbs")
    else:
        print("Invalid planet name. Please choose a planet from the list.")

# Ask user for input
planet_choice = input("Which planet to challenge next? ").capitalize()

# Calculate and print the new weight
new_planet_weight(earth_weight, planet_choice)