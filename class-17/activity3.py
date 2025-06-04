from tkinter import Tk, Label, Button, StringVar, messagebox

# Window on top of the window for rock, paper, scissors game

root = Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")

# Function to display the result of the game
def play_game(player_choice):
    import random

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! Computer chose {computer_choice}."
    else:
        result = f"You lose! Computer chose {computer_choice}."

    result_var.set(result)

# Variable to hold the result
result_var = StringVar()
result_var.set("Make your choice!")
# Labels to display the result
result_label = Label(root, textvariable=result_var, font=("Arial", 14), pady=20)
result_label.pack()

# Buttons for player choices
rock_button = Button(root, text="Rock", command=lambda: play_game("Rock"), width=10, font=("Garamond", 12))
rock_button.pack(pady=5)
paper_button = Button(root, text="Paper", command=lambda: play_game("Paper"), width=10, font=("Garamond", 12))
paper_button.pack(pady=5)
scissors_button = Button(root, text="Scissors", command=lambda: play_game("Scissors"), width=10, font=("Garamond", 12))
scissors_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()