
# * мог сделать намного лучше и понятнее, но из-за поэтапности ломается логика разработки
# * и довольно сложно подтраиваться каждый раз под требования задания
# * во многих моментах нужно перепысывать буквально пол, а то и больше програмы...

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


def main():
    cells_two_dim = list()
    n = 3
    for i in range(3):
        cells_two_dim.append(list('_')*3)

    print('-------')
    print('|' + ' '.join(cells_two_dim[0]) + '|')
    print('|' + ' '.join(cells_two_dim[1]) + '|')
    print('|' + ' '.join(cells_two_dim[2]) + '|')
    print('-------')

    is_play = True
    player = 'X'

    while is_play:
        try:
            i, j = input('Enter the coordinates:').split(' ')
        except:
            print('You should enter two numbers!')
            continue

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
            cells_two_dim[i-1][j-1] = player

        cells = []
        for el in cells_two_dim:
            cells.extend(el)
        
        print('-------')
        print('|' + ' '.join(list(cells[0:3])) + '|')
        print('|' + ' '.join(list(cells[3:6])) + '|')
        print('|' + ' '.join(list(cells[6:9])) + '|')
        print('-------')


        for i, opt in enumerate(WIN_OPT):
            if all(x=='X' for x in  [
                    cells[opt[0]],
                    cells[opt[1]],
                    cells[opt[2]]
                ]):
                print('Player x won')
                is_play = False
                break
            if all(x=='O' for x in  [
                    cells[opt[0]],
                    cells[opt[1]],
                    cells[opt[2]]
                ]):
                print('Player o won')
                is_play = False
                break
            if len(list(filter(lambda x: x != '_', cells))) == 9:
                print('Draw')
                break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
