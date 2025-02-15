#!/usr/bin/env python3
"""
PyGame Fundamentals Quiz
Difficulty: Progressive (Student → Junior)

This quiz tests understanding of core PyGame concepts through practical exercises.
"""

# Question 1: Basic Setup & Initialization
def q1_basic_setup():
    """
    Which essential PyGame function must be called before using any PyGame features?
    answer: pygame.init()

    What is the correct order of initialization for a basic PyGame program?
    
    # import the pygame module
    import pygame
    # initiates the game
    pygame.init()

    
    screen - pygame.display.set_mode((640,640))

    running = True


    """
    pass

# Question 2: Display Surface & Windows 
def q2_create_window():
    """
    Given this code snippet, what's missing to create a proper game window?
    """
    import pygame
    
    # Your code here to:
    # - Create a window of 800x600 pixels
    # - Set the window caption to "My Game"
    pass

# Question 3: Game Loop Structure
def q3_game_loop():
    """
    Complete the basic game loop structure that handles:
    - Event checking
    - Game state updates  
    - Screen rendering
    Include proper quit functionality
    """
    pass

# Question 4: Event Handling
def q4_fix_events():
    """
    What's wrong with this event handling code?
    """
    for event in pygame:
        if event == pygame.QUIT:
            quit()
        if event == pygame.K_SPACE:
            player.jump()

# Question 5: Drawing & Colors
def q5_drawing():
    """
    How would you:
    1. Draw a red rectangle at position (100, 100) with size 50x50
    2. Draw a blue circle at the center of the screen with radius 30
    3. Fill the background with white
    """
    pass

# Bonus Challenge
def bonus_animation():
    """
    Create a basic animation system that:
    - Moves a square from left to right
    - Bounces when it hits the screen edges
    - Changes color each time it bounces
    """
    pass

"""
Grading Criteria:
- Correctness of PyGame syntax
- Understanding of game loop concepts
- Proper event handling
- Efficient use of PyGame drawing functions  
- Clean code structure
"""

if __name__ == "__main__":
    print("Please attempt the questions above and submit your solutions for review.")
