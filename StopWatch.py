import tkinter as tk
from tkinter import messagebox
from time import time, strftime, gmtime
import random

# Variables to track time
start_time = None
running = False

# Quotes list
quotes = [
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't watch the clock; do what it does. Keep going."
]

def start():
    global start_time, running
    if not running:
        start_time = time()
        running = True
        update_timer()

def stop():
    global running
    running = False

def reset():
    global start_time, running
    running = False
    start_time = None
    label_timer.config(text="00:00:00")

def update_timer():
    if running:
        elapsed_time = time() - start_time
        formatted_time = strftime("%H:%M:%S", gmtime(elapsed_time))
        label_timer.config(text=formatted_time)
        window.after(100, update_timer)

def add_note():
    note = text_note.get(1.0, tk.END).strip()
    if note:
        listbox_notes.insert(tk.END, note)
        text_note.delete(1.0, tk.END)
    else:
        messagebox.showwarning("Warning", "Note cannot be empty!")

def delete_note():
    selected = listbox_notes.curselection()
    if selected:
        listbox_notes.delete(selected)
    else:
        messagebox.showwarning("Warning", "Please select a note to delete!")

def random_quote():
    quote = random.choice(quotes)
    messagebox.showinfo("Random Quote", quote)

# Create the main window
window = tk.Tk()
window.title("Enhanced Stopwatch with Features")

# Timer display
label_timer = tk.Label(window, text="00:00:00", font=("Helvetica", 24))
label_timer.pack()

# Stopwatch buttons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

button_start = tk.Button(frame_buttons, text="Start", command=start)
button_start.pack(side=tk.LEFT, padx=5)

button_stop = tk.Button(frame_buttons, text="Stop", command=stop)
button_stop.pack(side=tk.LEFT, padx=5)

button_reset = tk.Button(frame_buttons, text="Reset", command=reset)
button_reset.pack(side=tk.LEFT, padx=5)

# Notes section
frame_notes = tk.Frame(window)
frame_notes.pack(pady=10)

label_notes = tk.Label(frame_notes, text="Notes:")
label_notes.grid(row=0, column=0, sticky=tk.W)

text_note = tk.Text(frame_notes, height=4, width=30)
text_note.grid(row=1, column=0)

button_add_note = tk.Button(frame_notes, text="Add Note", command=add_note)
button_add_note.grid(row=2, column=0, pady=5)

listbox_notes = tk.Listbox(frame_notes, height=5, width=30)
listbox_notes.grid(row=3, column=0)

button_delete_note = tk.Button(frame_notes, text="Delete Note", command=delete_note)
button_delete_note.grid(row=4, column=0, pady=5)

# Random quote button
button_quote = tk.Button(window, text="Show Random Quote", command=random_quote)
button_quote.pack(pady=10)

# Run the application
window.mainloop()