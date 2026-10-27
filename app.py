import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
TARGET_SIZE = 40
GAME_TIME = 30

score = 0
time_left = GAME_TIME

# Functions
def move_target():
    x = random.randint(0, WIDTH - TARGET_SIZE)
    y = random.randint(50, HEIGHT - TARGET_SIZE)
    canvas.coords(target, x, y, x + TARGET_SIZE, y + TARGET_SIZE)

def hit_target(event):
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_target()

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time: {time_left}")
        root.after(1000, countdown)
    else:
        canvas.unbind("<Button-1>")
        canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text=f"Game Over!\nFinal Score: {score}",
            font=("Arial", 24, "bold"),
            fill="red"
        )

# Main Window
root = tk.Tk()
root.title("Catch The Target")
root.resizable(False, False)

# Labels
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(side=tk.LEFT, padx=20)

timer_label = tk.Label(root, text=f"Time: {GAME_TIME}", font=("Arial", 14))
timer_label.pack(side=tk.RIGHT, padx=20)

# Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

# Target
target = canvas.create_oval(
    100, 100,
    100 + TARGET_SIZE,
    100 + TARGET_SIZE,
    fill="red"
)

# Click detection
canvas.tag_bind(target, "<Button-1>", hit_target)

# Start Game
move_target()
countdown()

root.mainloop()
