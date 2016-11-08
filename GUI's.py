# Josh Dickey 11/8/16
# this program creates a guessing game

# this allows us to use a GUI
import tkinter

# this generates a random number
import random


def guessed():
    """this allows the user to guess the value and the computer tells the user whether or not they are right or wrong"""
    number_of_guesses = tries.get()
    number_of_guesses += 1
    tries.set(number_of_guesses)
    if answer.get() == computer.get():
        info.set("your guess is correct!")
    elif answer.get() >= computer.get():
        info.set("your guess is too high")
    elif answer.get() <= computer.get():
        info.set("your guess is too low")

# this allows us to use the GUI
root = tkinter.Tk()

# this inserts a line of text at top of GUI
guess_the_number = tkinter.Label(root, text="Can you guess the number?")
guess_the_number.grid(column=1, row=1)

# this inserts a line of text below the previous one
number_between = tkinter.Label(root, text="What number am I thinking of between 1 and 100?")
number_between.grid(column=1, row=2)

# this inserts a line of text below the previous one
goes_below = tkinter.Label(root, text="Your guess goes below")
goes_below.grid(column=1, row=3)

# these three things allow us to use values in our GUI
answer = tkinter.IntVar()

computer = tkinter.IntVar()

info = tkinter.StringVar()

# this displays whether or not the user guesses correctly
result = tkinter.Label(root, textvariable=info)
result.grid(column=2, row=1)

# this selects a random number between 1 and 100
computer.set(random.randint(1, 100))

# this defines tries and increases it by one each time you guess
tries = tkinter.IntVar()

# this creates a box for the user to enter a guess
user_answer = tkinter.Entry(root, textvariable=answer)
user_answer.grid(column=1, row=4)

# this creates a button that sends a guess
guess_button = tkinter.Button(root, text="Guess", command=guessed)
guess_button.grid(column=1, row=5)

# this is the label for the number of guesses
guess_label = tkinter.Label(root, text="number of guesses:")
guess_label.grid(column=2, row=4)

# this displays the number of guesses
guesses = tkinter.Label(root, text=0, textvariable=tries)
guesses.grid(column=2, row=5)


root.mainloop()
