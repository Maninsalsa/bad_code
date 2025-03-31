# # Interactive Python Fundamentals Quiz - Set 1: Basic Syntax and Data Types

# # What's the output of this code? 

# x = 5
# y = "3"
# print(str(x) + y)

# """The answer is 53. Reason being is adding two strings together is not addition, but
# string concantenation so it's basically just placing both values next to each other,
# no spaces."""

# # What will be the length of the numbers list? 

# numbers = [1,2,3]
# numbers.append([4,5])
# print(numbers)
# print(len(numbers))

# """appending a list within the append tuple will insert the whole list as a sublist inside
# the main list. Therefore printing the len will produce 4"""

# # What will be the output of this code?

# items = [1, 2, 3]
# items.extend([4, 5])
# print(items)
# items.append(6)
# print(items)
# items[1:3] = [8, 9]
# print(items)

# """items adds 4 and 5 as individual elements to the list. append 6 adds 6 after 5. Lastly,
# starting after the first index and before the 3rd, insert 8,9"""

# # Consider this code involving dictionaries and list comprehension:

# class GameObject:
#     def __init__(self, x, y, active=True):
#         self.x = x
#         self.y = y
#         self.active = active

# objects = [GameObject(i, i*2) for i in range(3)]
# positions = {f"obj{i}": (obj.x, obj.y) 
#             for i, obj in enumerate(objects) 
#             if obj.active}

# # print(positions)

# # What will be the output? 

# """ The class game object is defined by a tuple pair of coordinates, and whether or not
# it's active, which is a boolean flag for 'on/off.' Objects uses list comprehension to 
# create multiple game objects that have proportionately spaced y axis' so that when they're
#  created they spawn diagonally (see objects list comprehension). positions creates 
#  key:value pairs that map string keys to coordinate tuples. IF they are active
# In short, this code defines a game object's coordinates, and determines whether or not they're
# active. Objects generates multiple instances based on this list comprehension, position is a 
# logger of the positions of all current objects"""

# Q5 What will be the output of this code?

# class Player:
#     def __init__(self, x=0, y=0):
#         self.position = [x,y]
    
#     def move(self, dx, dy):
#         self.position[0] += dx
#         self.position[1] += dy

# players = {f"P{i}": Player(i, i) for i in range(2)}
# players["P0"].move(5,3)
# result = [p.position for p in players.values()]

# print(result)

# """The player class is defined by it's position and has an instance method of move, which
# updates the position by delta x and y. players creates a dict with i amount of key:value
# pairs with coordinates (i,i) in a given range. The player P0 coordinates is moved via the .move() instance method and result prints the coordinate calues in a 2D list. with this example, it should be [(5,3), (1,1)]"""

# # Q6 

# class Enemy:
#     def __init__(self, health=100):
#         self.health = health
#         self.active = True
    
#     def take_damage(self, amount):
#         self.health -= amount
#         if self.health <= 0:
#             self.active = False

# enemies = [Enemy() for _ in range(3)]  # Creates 3 enemies with 100 health each
# enemies[0].take_damage(50)             # First enemy now has 50 health
# enemies[1].take_damage(100)            # Second enemy has 0 health and becomes inactive

# active_enemies = [e.health for e in enemies if e.active]
# print(active_enemies)

# # What is printed? 

# """The enemy class has two instance variables, health and active.
# # Initial state
# enemies = [Enemy() for _ in range(3)]
# # All have health=100 and active=True

# # After damages:
# enemies[0].take_damage(50)    # health=50,  active=True
# enemies[1].take_damage(100)   # health=0,   active=False
# # enemies[2] unchanged        # health=100, active=True

# # Key line:
# active_enemies = [e.health for e in enemies if e.active]
# # Only includes health values where active=True
# # So enemy[1] is filtered out because active=False
# # Result: [50, 100]
# """

# Q7 What will be the output of this code?

class PowerUp:
    def __init__(self, type_name: str, duration: float):
        self.type = type_name
        self.duration = duration
        self.active = False

    def activate(self):
        self.active = True
    
    def update(self, delta_time):
        if self.active:
            self.duration -= delta_time
            if self.duration <= 0:
                self.active = False

powerups = [PowerUp("speed", 10), PowerUp("sheild", 5)]
powerups[0].update(6)
powerups[1].activate()
powerups[1].update(2)

active_effects = [(p.type, p.duration) for p in powerups if p.active]
print(active_effects)