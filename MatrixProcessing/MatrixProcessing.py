import random
from warnings import showwarning


class Matrix:
    def __init__(self, rows=None, cols=None, matrix=[]) -> None:
        if matrix:
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])
        elif rows and cols:
            self.matrix = []
            self.rows = rows
            self.cols = cols

            for _ in range(self.rows):
                self.matrix.append([])
                for _ in range(self.cols):
                    self.matrix[-1].append(random.randint(-10, 11))
        else:
            self.matrix = []
            self.rows = 0
            self.cols = 0
            return

    def sum(self, matrix2):
        if self.rows != matrix2.rows\
                and self.cols != matrix2.cols:
            print('ERROR: cant sum different shape matrix')

        new_matrix = []

        for i in range(self.rows):
            new_matrix.append([])
            for j in range(self.cols):
                new_matrix[-1].append((self.matrix[i][j]) +
                                      (matrix2.matrix[i][j]))

        return Matrix(matrix=new_matrix)

    def show_matrix(self):
        print('\nPrinting matrix')
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end='\t')
            print('')

        return self

    def trans_from_str(self):
        self.rows, self.cols = [int(x)
                                for x in input('Size(rows, cols):').split()]

        for i in range(self.rows):
            self.matrix.append([int(x) for x in input(
                f'Enter row number {i+1}: ').split()])

        return self

    def multiply_by_factor(self, factor):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= factor

        return self

    def multiply_on_matrix(self, matrix2):
        new_matrix = []
        sum_ = 0

        if self.rows == matrix2.cols:
            for i in range(self.rows):
                new_matrix.append([])

                for k in range(matrix2.cols):
                    for j in range(matrix2.rows):
                        sum_ += self.matrix[i][j] * matrix2.matrix[j][k]

                    new_matrix[-1].append(sum_)
                    sum_ = 0

            return Matrix(matrix=new_matrix)
        else:
            print('ERROR: cant mupltiply this matrices')

    def __str__(self) -> str:
        self.show_matrix()
        return ''


def main():
    while True:
        choice = input('1. Add matrices\n'
                       '2. Multiply matrix by a constant\n'
                       '3. Multiply matrices\n'
                       '0. Exit\nYour choice: ')
        if choice == '1':
            matrix1 = Matrix.trans_from_str(Matrix())
            matrix2 = Matrix.trans_from_str(Matrix())
            print(matrix1.sum(matrix2))
        if choice == '2':
            factor = int(input('Enter your factor to mupltiply matrix: '))
            matrix1 = Matrix.trans_from_str(Matrix()).multiply_by_factor(factor).show_matrix()
        if choice == '3':
            matrix1 = Matrix.trans_from_str(Matrix())
            matrix2 = Matrix.trans_from_str(Matrix())
            print(matrix1.multiply_on_matrix(matrix2))
        if choice == '0':
            break

if __name__ == "__main__":
    main()
