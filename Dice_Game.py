"""
Dice Game Assignment 4
"""

import random

Personal_lucky_number = 3


def roll():
    dice_roll = random.randint(0,6)
    return dice_roll


def main():
    roll()
    

if __name__ == "__main__":
    main()