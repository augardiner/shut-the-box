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
        print(f'Dice 1: {dice1}\n\nTotal: {diceTotal}\n')
    else:
        diceTotal = dice1 + dice2
        print(f'Dice 1: {dice1}\nDice 2: {dice2}\n\nTotal: {diceTotal}\n')
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
        try:
            if numsToDropInput == '':
                return False
            numsToDropInput = numsToDropInput.strip('()')
            numsToDropInput = numsToDropInput.split(',')
            numsToDropInput = [int(i) for i in numsToDropInput]
        except:
            print('Invalid Input.\n')
            continue
        if sum(numsToDropInput) != diceTotal:
            print('Invalid Sum. Try Again.\n')
            continue
        for num in numsToDropInput:
            if num in numbers:
                numsToDrop.append(num)
                loop = False
            else:
                print(f'There is no {num} available. Try again.\n')
                loop = True
                break
        if loop:
            continue
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
        print(f'End Game.\nPoint Total = {pointSum}\n')
        break
    numsToDrop = get_nums_to_drop(numbers, diceTotal)
    if not numsToDrop:
        print(f'End Game.\nPoint Total = {pointSum}\n')
        break
    numbers = get_new_numbers(numbers, numsToDrop)
    if len(actualNumbers) == 0:
        print_board(numbers)
        print('Congratulations! You shut the box!\n')
        break
    print_board(numbers)