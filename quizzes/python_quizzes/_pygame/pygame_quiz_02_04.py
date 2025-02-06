# PYGAME QUIZ

"""
1. What is the correct way to initialize Pygame in your code?
a) pygame.init()
b) pygame.start()
c) pygame.begin()
d) pygame.setup()

Answer: a) pygame.init()
Explanation: pygame.init() initializes all Pygame modules and must be called before using any other Pygame functions.

2. How do you create a window surface in Pygame?
a) pygame.display.create((width, height))
b) pygame.window.set_mode((width, height))
c) pygame.display.set_mode((width, height))
d) pygame.screen.create((width, height))

Answer: c) pygame.display.set_mode((width, height))
Explanation: This creates a window of specified dimensions and returns a Surface object representing the display.

3. Which method is used to update the display window in Pygame?
a) pygame.screen.refresh()
b) pygame.display.update()
c) pygame.window.flip()
d) pygame.display.show()

Answer: b) pygame.display.update()
Explanation: pygame.display.update() refreshes the display to show any changes made to the surface.

4. How do you handle events in Pygame?
a) pygame.event.check()
b) pygame.event.get()
c) pygame.event.handle()
d) pygame.event.poll()

Answer: b) pygame.event.get()
Explanation: pygame.event.get() returns a list of all pending events from the event queue.

5. What is the correct way to load an image in Pygame?
a) pygame.image.get("image.png")
b) pygame.load_image("image.png")
c) pygame.image.load("image.png")
d) pygame.surface.load("image.png")

Answer: c) pygame.image.load("image.png")
Explanation: pygame.image.load() loads an image from a file and returns a Surface object.

6. How do you create a rectangle object in Pygame?
a) pygame.Rect(x, y, width, height)
b) pygame.Rectangle(x, y, width, height)
c) pygame.create_rect(x, y, width, height)
d) pygame.box(x, y, width, height)

Answer: a) pygame.Rect(x, y, width, height)
Explanation: pygame.Rect() creates a rectangle object with the specified position and dimensions.

7. What method is used to draw a filled rectangle on a surface?
a) surface.rectangle(rect, color)
b) surface.draw.rect(rect, color)
c) surface.fill_rect(rect, color)
d) surface.draw_rectangle(rect, color)

Answer: b) surface.draw.rect(rect, color)
Explanation: pygame.draw.rect() draws a rectangle on the specified surface with the given color.

8. How do you control the frame rate in Pygame?
a) pygame.time.Clock().tick(fps)
b) pygame.fps.set(fps)
c) pygame.display.set_fps(fps)
d) pygame.clock.set(fps)

Answer: a) pygame.time.Clock().tick(fps)
Explanation: Creating a Clock object and using tick() helps control the game's frame rate.

9. Which method is used to detect keyboard input in Pygame?
a) pygame.key.pressed()
b) pygame.key.get_pressed()
c) pygame.input.get_keys()
d) pygame.keyboard.state()

Answer: b) pygame.key.get_pressed()
Explanation: Returns a list of boolean values representing the state of all keyboard buttons.

10. How do you play a sound effect in Pygame?
a) pygame.sound.play("sound.wav")
b) pygame.audio.load("sound.wav").play()
c) pygame.mixer.Sound("sound.wav").play()
d) pygame.music.play("sound.wav")

Answer: c) pygame.mixer.Sound("sound.wav").play()
Explanation: Creates a Sound object from the file and plays it using the play() method.
"""

# Example implementation of a quiz game using these questions
def run_pygame_quiz():
    questions = [
        {
            "question": "What is the correct way to initialize Pygame in your code?",
            "options": ["pygame.init()", "pygame.start()", "pygame.begin()", "pygame.setup()"],
            "correct": 0
        },
        # Add other questions similarly
    ]
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(q["question"])
        for j, opt in enumerate(q["options"]):
            print(f"{chr(97 + j)}) {opt}")
        
        answer = input("\nYour answer (a/b/c/d): ").lower()
        if ord(answer) - ord('a') == q["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['options'][q['correct']]}")
    
    print(f"\nFinal score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_pygame_quiz()