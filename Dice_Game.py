"""
Dice Game Assignment 4
"""

import random

Personal_lucky_number = 3


def roll():
    dice_roll = random.randint(0,6)
    return dice_roll

lucky_number = 3
dice_value1 = roll()
dice_value2 = roll()


def play_game(lucky_number, dice_value1, dice_value2):

    total_roll = dice_value1 + dice_value2

    if dice_value1 == lucky_number and dice_value2 == lucky_number:
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
    play_game()


if __name__ == "__main__":
    main()