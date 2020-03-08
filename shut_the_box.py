from random import randint
import itertools

def print_board(numbers):

    numbersString = [str(i) for i in numbers]
    divider = '|'
    board = divider.join(numbersString)
    print('='*19)
    print('|' + board + '|')
    print(('='*19))

def roll_dice(actualNumbers):

    dice1 = randint(1,6)
    dice2 = randint(1,6)

    if max(actualNumbers) <= 6:
        diceTotal = dice1
        print('Dice 1: {}\n\nTotal: {}\n'.format(dice1, diceTotal))
    else:
        diceTotal = dice1 + dice2
        print('Dice 1: {}\nDice 2: {}\n\nTotal: {}\n'.format(dice1, dice2, diceTotal))
    return diceTotal

def check_roll(actualNumbers, diceTotal):
    
    for i in range(0, len(actualNumbers)+1):
        for combo in itertools.combinations(actualNumbers, i):
            if sum(combo) == diceTotal:
                return 'pass', sum(actualNumbers)
    else: 
        return 'fail', sum(actualNumbers)

def get_nums_to_drop(numbers, diceTotal):
    
    numsToDrop = []

    while True:

        numsToDropInput = input('Enter which numbers you would like to drop, separated by a comma:\n>>>')

        if numsToDropInput == '':
            return False        
        try:
            if sum(numsToDropInput)!= diceTotal:
                print('Invalid Sum. Try again\n')
                continue
            for num in numsToDropInput:
                if num not in numbers:
                    print('There is no {} available. Try again.\n'.format(num))
                continue
            numsToDrop = [i for i in numsToDropInput]
            return numsToDrop
        except:
            if numsToDropInput != diceTotal or numsToDropInput > 9:
                print('Invalid Sum. Try again\n')
                continue
            elif numsToDropInput not in numbers:
                print('There is no {} available. Try again.\n'.format(numsToDropInput))
                continue
            else:
                numsToDrop.append(numsToDropInput)
                return numsToDrop

def get_new_numbers(numbers, numsToDrop):

    newNumbers = []
    for num in numbers:
        if num not in numsToDrop:
            newNumbers.append(num)
        else:
            newNumbers.append('_')
    return newNumbers

numbers = [i for i in range(1,10)]
print_board(numbers)

while True:

    actualNumbers = [i for i in numbers if type(i)==int]
    diceTotal = roll_dice(actualNumbers)
    resultOfCheck, pointSum = check_roll(actualNumbers, diceTotal)
    if resultOfCheck == 'fail':
        print('End Game.\nPoint Total = {}\n'.format(pointSum))
        break
    numsToDrop = get_nums_to_drop(numbers, diceTotal)
    numbers = get_new_numbers(numbers, numsToDrop)
    if len(actualNumbers) == 0:
        print_board(numbers)
        print('Congratulations! You shut the box!\n')
        break
    print_board(numbers)