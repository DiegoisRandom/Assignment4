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

def main():
    roll_test()

if __name__ == "__main__":
    main()



