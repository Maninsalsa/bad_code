#  Intermediate Concepts Quiz: Bridging the Gap


"""# Question 1
What is the primary advantage of using classes with inheritance for game objects like projectiles?

A) It makes the code run faster
B) It reduces the amount of code needed by reusing common functionality
C) It makes debugging easier by isolating each object in its own file
D) It's required by 's syntax rules"""

"""# Question 2
What does this code do and what concept does it demonstrate?
"""

class Weapon:
    def fire(self):
        print("Generic firing mechanism")

class Pistol(Weapon):
    def fire(self):
        print("Pistol fires a bullet")

class Shotgun(Weapon):
    def fire(self):
        print("Shotgun fires multiple pellets")
        
weapons = [Pistol(), Shotgun()]
for weapon in weapons:
    weapon.fire()


# A) Function overloading
# B) Method overriding
# C) Multiple inheritance
# D) Duck typing

## Question 3
# When working with game objects that need to store their position, which approach is more efficient and why?

# A) Store x and y as separate variables
# B) Store position as a tuple (x, y)
# C) Store position as a list [x, y]
# D) Use a Vector2 class that handles vector operations

## Question 4
# What is the purpose of the following code in a game context?

def __init__(self):
    self._health = 100
    
@property
def health(self):
    return self._health
    
@health.setter
def health(self, value):
    old_health = self._health
    self._health = max(0, min(value, 100))
    if self._health <= 0 and old_health > 0:
        self.on_death()


# A) It's just a complicated way to store a number
# B) It constrains health values and triggers events when they change
# C) It makes the health variable private and inaccessible
# D) It's a way to save memory when storing health values

## Question 5
# What would be a benefit of using this pattern for managing game entities?

class EntityManager:
    def __init__(self):
        self.entities = []
        
    def add(self, entity):
        self.entities.append(entity)
        
    def update(self, dt):
        for entity in self.entities[:]:  # Using a copy of the list
            entity.update(dt)
            if not entity.alive:
                self.entities.remove(entity)


# A) It prevents the game from crashing if an entity is removed during iteration
# B) It makes the code run faster
# C) It allows entities to communicate with each other
# D) It reduces memory usage

## Question 6
# What does this code demonstrate, and why is it useful in game development?

from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def update(self, dt):
        pass
        
    @abstractmethod
    def render(self, surface):
        pass


# A) It creates placeholder methods that do nothing
# B) It forces derived classes to implement specific methods
# C) It makes the code run faster by using the ABC module
# D) It prevents the GameObject class from being used directly

## Question 7
# In the context of a collision system, what is the purpose of using a "hitbox" that's different from the visual representation?

# A) To make collision detection more accurate to what the player sees
# B) To simplify collision calculations with regular shapes
# C) To allow the game to run faster by using smaller collision areas
# D) All of the above

## Question 8
# What is the difference between these two approaches to object creation?

# Approach 1:

# bullet = Bullet(player.position, player.direction)


# Approach 2:

# bullet_manager.create_bullet(player.position, player.direction)


# A) There is no significant difference
# B) Approach 1 is faster but less organized
# C) Approach 2 enables centralized management of bullets
# D) Approach 1 is the only valid  syntax

## Question 9
# What does this code pattern demonstrate and why is it useful for game states?

class GameState:
    def __init__(self, game):
        self.game = game
        
    def update(self, dt):
        pass
        
    def render(self, surface):
        pass
        
    def handle_event(self, event):
        pass
        
    def enter(self):
        pass
        
    def exit(self):
        pass


# A) It's a template for functions that don't do anything
# B) It defines a common interface for different game states
# C) It creates a game that doesn't actually run
# D) It's a way to organize code in multiple files

## Question 10
# # What would be the advantage of using the following approach for handling different types of projectiles?

class ProjectileManager:
    def __init__(self):
        self.projectile_types = {
            "bullet": BulletClass,
            "laser": LaserClass,
            "missile": MissileClass
        }
    
    def create_projectile(self, type_name, **kwargs):
        if type_name in self.projectile_types:
            return self.projectile_types[type_name](**kwargs)
        else:
            raise ValueError(f"Unknown projectile type: {type_name}")


# A) It allows creating projectiles without knowing their specific class
# B) It makes the code run faster
# C) It prevents errors when creating projectiles
# D) It uses less memory than creating instances directly

