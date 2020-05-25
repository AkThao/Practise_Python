from time import sleep
import sys


def start_game():
    turns = 3
    player_1_score = 0
    player_2_score = 0

    print("""\n\n********************************************
****  WELCOME TO ROCK, PAPER, SCISSORS  ****
********************************************\n\n""")

    sleep(1)

    while(turns > 0):
        player_1_choice = input("""Player 1, enter your choice:
r = rock
p = paper
s = scissors\n""").lower()

        player_2_choice = input("""\nPlayer 2, enter your choice:
r = rock
p = paper
s = scissors\n""").lower()

        sleep(0.5)
        print("\nProcessing....\n")
        sleep(0.5)

        if player_1_choice == 'r' and player_2_choice == 'p': player_2_score += 1
        if player_1_choice == 'r' and player_2_choice == 's': player_1_score += 1
        if player_1_choice == 'p' and player_2_choice == 'r': player_1_score += 1
        if player_1_choice == 'p' and player_2_choice == 's': player_2_score += 1
        if player_1_choice == 's' and player_2_choice == 'r': player_2_score += 1
        if player_1_choice == 's' and player_2_choice == 'p': player_1_score += 1

        turns -= 1

    print("\nCollecting results....\n")
    sleep(1)

    if player_1_score == player_2_score:
        print(f"\nFinal score is:\nPlayer 1 = {player_1_score}\nPlayer 2 = {player_2_score}")
        sleep(0.5)
        print("\nIt's a draw!\n")
    elif player_1_score > player_2_score:
        print(f"\nFinal score is:\nPlayer 1 = {player_1_score}\nPlayer 2 = {player_2_score}")
        sleep(0.5)
        print("\nPlayer 1 wins!\n")
    else:
        print(f"\nFinal score is:\nPlayer 1 = {player_1_score}\nPlayer 2 = {player_2_score}")
        sleep(0.5)
        print("\nPlayer 2 wins!\n")

    sleep(1)
    print("""\n\n************************
****  End of game.  ****
************************\n\n""")

    sleep(1)

while(1):
    choice = int(input("""\nEnter your choice:
1 = start a new game
2 = quit game\n\n"""))

    if choice == 1:
        start_game()
    elif choice == 2:
        print("Exiting game....")
        sleep(1)
        break
        sys.exit()