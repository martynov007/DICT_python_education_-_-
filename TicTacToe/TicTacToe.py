def main():
    cells = input('Enter cells:')

    if len(cells) != 9:
        print('Only 9 symbols')
        return None
    # * проверка вхождения лишних букв в строку
    elif g := list(filter(lambda x: x not in ['X', 'O', '_'], cells)):
        print(', '.join(g) + ' shouldn\'t be there')
        return None

    print('-------')
    print('|' + ' '.join(list(cells[0:3])) + '|')
    print('|' + ' '.join(list(cells[3:6])) + '|')
    print('|' + ' '.join(list(cells[6:9])) + '|')
    print('-------')

    cells_two_dim = [list(cells[0:3]), list(cells[3:6]), list(cells[6:9])]

    while True:
        i, j = input('Enter the coordinates:').split(' ')

        if not i.isnumeric() or not j.isnumeric():
            print('You should enter numbers!')
            continue

        i, j = (int(i), int(j))
        if (i < 1 or i > 3)\
            or (j < 1 or j > 3):
            print('Coordinates should be from 1 to 3!')
            continue
        if cells_two_dim[i-1][j-1] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            cells_two_dim[i-1][j-1] = 'X'
        break

    cells = []
    for el in cells_two_dim:
        cells.extend(el)
    
    print('-------')
    print('|' + ' '.join(list(cells[0:3])) + '|')
    print('|' + ' '.join(list(cells[3:6])) + '|')
    print('|' + ' '.join(list(cells[6:9])) + '|')
    print('-------')
    
    WIN_OPT = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    X_won = False
    O_won = False
    for i, opt in enumerate(WIN_OPT):
        if any(x=='_' for x in cells):
                print('Game not finished')
                break
        if all(x=='X' for x in  [
                cells[opt[0]],
                cells[opt[1]],
                cells[opt[2]]
            ]):
            X_won = True
        if all(x=='O' for x in  [
                cells[opt[0]],
                cells[opt[1]],
                cells[opt[2]]
            ]):
            O_won = True

    if X_won and O_won:
        print('Imppossible')
    elif X_won:
        print('Player x won')
    elif O_won:
        print('Player O won')
    else:
        print('Draw')
if __name__ == "__main__":
    main()
