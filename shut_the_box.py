from random import randint, sample
import itertools

DICE_DICT = {
    1: '\u2680',
    2: '\u2681',
    3: '\u2682',
    4: '\u2683',
    5: '\u2684',
    6: '\u2685',
}

def print_board(numbers, d1, d2):

    numbersString = [str(i) for i in numbers]
    divider = '|'
    board = divider.join(numbersString)
    print('|'+'='*19+'|')
    print('|'+'|'+board+'|'+'|')
    print('|'+'='*19+'|')
    d1_row, d2_row = sample(range(0, 3), 2)
    d1_col, d2_col = sample(range(0, 19), 2)
    d1_remain = 18-d1_col
    d2_remain = 18-d2_col
    for i in range(3):
        if i == d1_row and d1 != None:
            print('|' + ' '*d1_col + DICE_DICT[d1] + ' '*d1_remain + '|')
        if i == d2_row and d2 != None:
            print('|' + ' '*d2_col + DICE_DICT[d2] + ' '*d2_remain + '|')
        else:
            print('|'+' '*19+'|') 
    print('|'+'='*19+'|')
    d2_p = d2 if d2 else '-'
    total = d1+d2 if d2 else d1
    print(f'  D1:{d1} D2:{d2_p} Total:{total}')


def roll_dice(actualNumbers):

    d1 = randint(1,6)
    d2 = randint(1,6)

    if max(actualNumbers) <= 6:
        diceTotal = d1
        d2 = None
    else:
        diceTotal = d1 + d2
    return d1, d2, diceTotal

def check_roll(actualNumbers, diceTotal):
    
    for i in range(1, len(actualNumbers)+1):
        for combo in itertools.combinations(actualNumbers, i):
            if sum(combo) == diceTotal:
                return 'pass', sum(actualNumbers)
    else: 
        return 'fail', sum(actualNumbers)

def get_nums_to_drop(numbers, diceTotal):
    
    numsToDrop = []
    invalid = True
    while invalid:

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
        inList = []
        for num in numsToDropInput:
            if num in inList:
                print('You can not repeat numbers. Try again.\n')
                invalid = True
                break
            else:
                inList.append(num)            
            if num not in numbers:
                print(f'There is no {num} available. Try again.\n')
                invalid = True
                break
            else:
                numsToDrop.append(num)
                invalid = False
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

while True:

    actualNumbers = [i for i in numbers if type(i)==int]
    d1, d2, diceTotal = roll_dice(actualNumbers)
    print_board(numbers, d1, d2)
    resultOfCheck, pointSum = check_roll(actualNumbers, diceTotal)
    if resultOfCheck == 'fail':
        print(f'Game Over. Point Total={pointSum}')
        break
    numsToDrop = get_nums_to_drop(numbers, diceTotal)
    if not numsToDrop:
        print(f'Game Over. Point Total={pointSum}')
        break
    numbers = get_new_numbers(numbers, numsToDrop)
    if all(i == '_' for i in numbers):
        print_board(numbers, None, None)
        print('Congratulations! You shut the box!')
        break