from tkinter import Tk, Label, Button, StringVar, messagebox, Toplevel
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        self.user_choice = StringVar()
        self.computer_choice = StringVar()
        self.result = StringVar()
        
        Label(root, text="Choose your move:").pack()
        
        Button(root, text="Rock", command=lambda: self.play("Rock")).pack()
        Button(root, text="Paper", command=lambda: self.play("Paper")).pack()
        Button(root, text="Scissors", command=lambda: self.play("Scissors")).pack()
        
    def play(self, user_move):
        choices = ["Rock", "Paper", "Scissors"]
        computer_move = random.choice(choices)
        
        self.user_choice.set(f"Your choice: {user_move}")
        self.computer_choice.set(f"Computer's choice: {computer_move}")
        
        if user_move == computer_move:
            self.result.set("Result: It's a tie!")
        elif (user_move == "Rock" and computer_move == "Scissors") or \
             (user_move == "Paper" and computer_move == "Rock") or \
             (user_move == "Scissors" and computer_move == "Paper"):
            self.result.set("Result: You win!")
        else:
            self.result.set("Result: Computer wins!")
        
        self.show_result()
    
    def show_result(self):
        top = Toplevel(self.root)
        top.title("Game Result")
        top.geometry("300x150")
        top.attributes('-topmost', True)
        
        Label(top, textvariable=self.user_choice).pack()
        Label(top, textvariable=self.computer_choice).pack()
        Label(top, textvariable=self.result).pack()
        
        Button(top, text="OK", command=top.destroy).pack()

root = Tk()
app = RockPaperScissors(root)
root.mainloop()