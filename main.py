import os
import time
import random


game_items = {
        "paper": {"win": "rock", "lose": "scissors"},
        "scissors": {"win": "paper", "lose": "rock"},
        "rock": {"win": "scissors", "lose": "paper"}
}

play_no = 0  # Record the number of times plays played

os.system("clear")
while True:
    if play_no > 5:
        os.system("clear")
        play_no = 0

    choice = random.choice(list(game_items.keys()))
    play = input("Guess a play: ").lower()

    if play == choice:
        print("I T S  A  T I E ! ! !")
        continue
    
    elif play == "quit" or play == "exit":
        print("E X I T E D ! ! !")
        break

    else:
        player_choice = game_items.get(play)
        if not player_choice:
            print("You can only choose between ROCK, PAPER and SCISSORS")
            continue
        for key, value in player_choice.items():
            if choice == value:
                print(f"{play} <--> {choice}")
                if key == 'win':
                    print("Y O U  W O N ! ! !")
                else:
                    print("Y O U  L O S E ! ! !")

        play_no += 1
        time.sleep(2)

