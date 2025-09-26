import Dice_Game

import random

def roll_test():

    """ Test 1 """

    #Setup:
    random.seed(1)

    expected = 1

    #Invoke:
    actual = Dice_Game.roll()

    #Analyze
    assert actual == expected

    #Result:
    print(str(expected))
    print(str(actual))
    print("Testing for roll test passed.")

def test_play_game():
    #Setup

    dice_value1 = 3
    dice_value2 = 3
    lucky_number = 3

    expected = "Amazing! You rolled your lucky number twice and won!"

    #Invoke

    actual = Dice_Game.play_game(lucky_number, dice_value1, dice_value2)

    #Analyze

    assert actual == expected

    #Result
    print("Testing for play game have passed.")


def main():
    roll_test()
    test_play_game()

if __name__ == "__main__":
    main()



