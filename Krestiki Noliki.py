Board={'7': ' ', '8': ' ', '9': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '1': ' ', '2': ' ', '3': ' '}
def printBoard(boar):
    print(boar['7'] + '|' + boar['8'] + '|' + boar['9'])
    print('-+-+-')
    print(boar['4'] + '|' + boar['5'] + '|' + boar['6'])
    print('-+-+-')
    print(boar['1'] + '|' + boar['2'] + '|' + boar['3'])
choice='X'
for i in range(9):
    printBoard(Board)
    print('Ход для ' + choice + '.Куда вы хотите поставить?')
    move=input()
    Board[move]=choice
    if choice =='X':
        choice='O'
    else:
        choice='X'
    
    if 'X' in Board['7'] and 'X' in Board['8'] and 'X' in Board['9'] or 'X' in Board['4'] and 'X' in Board['5'] and 'X' in Board['6'] or 'X' in Board['1'] and 'X' in Board['2'] and 'X' in Board['3'] or 'X' in Board['7'] and 'X' in Board['4'] and 'X' in Board['1'] or 'X' in Board['8'] and 'X' in Board['5'] and 'X' in Board['2'] or 'X' in Board['3'] and 'X' in Board['6'] and 'X' in Board['9'] or 'X' in Board['1'] and 'X' in Board['5'] and 'X' in Board['9'] or 'X' in Board['3'] and 'X' in Board['5'] and 'X' in Board['7']:
        printBoard(Board)
        print('Игрок игравший X выиграл!')
        break
    elif 'O' in Board['7'] and 'O' in Board['8'] and 'O' in Board['9'] or 'O' in Board['4'] and 'O' in Board['5'] and 'O' in Board['6'] or 'O' in Board['1'] and 'O' in Board['2'] and 'O' in Board['3'] or 'O' in Board['7'] and 'O' in Board['4'] and 'O' in Board['1'] or 'O' in Board['8'] and 'O' in Board['5'] and 'O' in Board['2'] or 'O' in Board['3'] and 'O' in Board['6'] and 'O' in Board['9'] or 'O' in Board['1'] and 'O' in Board['5'] and 'O' in Board['9'] or 'O' in Board['3'] and 'O' in Board['5'] and 'O' in Board['7']:
        printBoard(Board)
        print('Игрок игравший O выиграл!')
        break
print('Нажмите Enter для заверщения игры')
input()
printBoard(boar)
