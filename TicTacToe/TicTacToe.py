def main():
    cells = input('Enter cells:')

    if len(cells) != 9:
        print('Only 9 symbols')
        return None
    # * проверка вхождения лишних букв в строку
    elif g:=list(filter(lambda x: x not in ['X', 'O', '_'], cells)):
        print(', '.join(g) + ' shouldn\'t be there')
        return None

    print('-------')
    print('|' + ' '.join(list(cells[0:3])) + '|')
    print('|' + ' '.join(list(cells[3:6])) + '|')
    print('|' + ' '.join(list(cells[6:9])) + '|')
    print('-------')

if __name__ == "__main__":
    main()