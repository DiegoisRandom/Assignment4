"""
Dice Game Assignment 4
"""

import random

Personal_lucky_number = 3


def roll():
    dice_roll = random.randint(0,6)
    return dice_roll

lucky_number = 3
d1 = roll()
d2 = roll()


def play_game(lucky_number, d1, d2):

    total_roll = d1 + d2

    if d1 == lucky_number and d2 == lucky_number:
        return "Amazing! You rolled your lucky number twice and won!"
    elif total_roll == 12:
        return "Jackpot! You won the grand prize!"
    elif 10 <= total_roll <=11:
        return "Great Roll! You won a large prize!"
    elif 7 <= total_roll <= 9:
        return "Nice Roll! You won a medium prize."
    elif 5 <= total_roll <= 6:
        return "Decent. You won a small prize."
    elif 1 <=  total_roll <= 4:
        return "Better luck next time."
    

def main():
    lucky_number = int(input("Enter a lucky number: "))
    d1 = roll()
    d2 = roll()
    total = d1 + d2

    print("" + str(total) + " - " + str(play_game(lucky_number, d1, d2)))
    
    lucky_number = int(input("Enter a lucky number: "))
    d1 = roll()
    d2 = roll()
    total = d1 + d2

    print("" + str(total) + " - " + str(play_game(lucky_number, d1, d2)))


    lucky_number = int(input("Enter a lucky number: "))
    d1 = roll()
    d2 = roll()
    total = d1 + d2

    print("" + str(total) + " - " + str(play_game(lucky_number, d1, d2)))



if __name__ == "__main__":
    main()