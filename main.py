import random
# Random number 0-2 W 

options = ["S", "P", "R"]
options_for_print = ["Scissors", "Paper", "Rock"]
userchoice = input("What do you choose? S for scissors, P for papers, R for rock: ")
random_number = random.randint(0, 2)
computer_choice = options[random_number]

# Cases for tie, win else lose
if userchoice.upper() not in options:
    print("You have entered an invalid option")
else:
    if userchoice == computer_choice:
        print(f"Computer chose {options_for_print[random_number]} you tied")
    elif userchoice.upper() == "S" and computer_choice == "P":
        print(f"Computer chose {options_for_print[random_number]} you win")
    elif userchoice.upper() == "P" and computer_choice == "R":
        print(f"Computer chose {options_for_print[random_number]} you win")
    elif userchoice.upper() == "R" and computer_choice == "S":
        print(f"Computer chose {options_for_print[random_number]} you win")
    else:
        print(f"Computer chose {options_for_print[random_number]} you lose")