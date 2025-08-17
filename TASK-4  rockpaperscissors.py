import random
choices = ["rock", "paper","scissors"]
user_score = 0
computer_score=0

while True:
    user_choice = input("Enter rock,paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice.Try AGAIN")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose : {user_choice}")
    print(f"computer chose:{computer_choice}")
    
    if user_choice == computer_choice:
        print("Its tie")
    elif ((user_choice == "rock" and computer_choice == " scissors") or  (user_choice == "scissors" and computer_choice=="paper") or(user_choice=="paper" and computer_choice == "rock")):
        print("you win")
        user_score += 1
    else:
        print("computer wins")
        computer_score +=1

    print(f"score -> you : {user_score} | computer: {computer_score}")
    
    play_again = input("do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing!")
        break

