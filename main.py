# For storing user choices
choices = []

# For initializing the board with numbers
for i in range(0, 9):
    choices.append(str(i))

def clearBoard():
    for i in range(0, 9):
        choices[i] = str(i)

def printBoard():
    print('\n=============')
    print('| ' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] + ' |')
    print('=============')
    print('| ' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] + ' |')
    print('=============')
    print('| ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] + ' |')
    print('=============\n')

def wygranie_x():
    for index in range(0, 3):
        if (choices[index * 3] == choices[((index * 3) + 1)] and choices[index * 3] == choices[((index * 3) + 2)] == 'X'):
            winner = 'X'
            printBoard()
            clearBoard()
            return winner

        # For [0,3,6], [1,4,7], [2,5,8]
        if (choices[index] == choices[index + 3] and choices[index + 3] == choices[index + 6] == 'X'):
            winner = 'X'
            printBoard()
            clearBoard()
            return winner


        if ((choices[0] == choices[4] and choices[4] == choices[8] == 'X') or
                (choices[2] == choices[4] and choices[4] == choices[6] == 'X')):
            winner = 'X'
            printBoard()
            clearBoard()
            return winner


def wygranie_o():
    for index in range(0, 3):
        if (choices[index * 3] == choices[((index * 3) + 1)] and choices[index * 3] == choices[((index * 3) + 2)] == 'O'):
            winner = 'O'
            printBoard()
            clearBoard()
            return winner

        # For [0,3,6], [1,4,7], [2,5,8]
        if(choices[index] == choices[index + 3] and choices[index + 3] == choices[index + 6] == 'O'):
            winner = 'O'
            printBoard()
            clearBoard()
            return winner

        if((choices[0] == choices[4] and choices[4] == choices[8] == 'O') or
          (choices[2] == choices[4] and choices[4] == choices[6]) == 'O'):
            winner = 'O'
            printBoard()
            clearBoard()
            return winner


def ruch(player, x):
    if walidacja_ruchu(x) == 0:
        choices[x] = player
    else:
        print("To pole jest zajęte! Wybierz inny nr pola")
        return 1


def walidacja_ruchu(x):
    if choices[x] == 'O' or choices[x] == 'X':
        return 1
    else:
        return 0


