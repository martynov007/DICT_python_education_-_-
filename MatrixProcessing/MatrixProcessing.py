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

    def transpose_by_side_line(self):
        for i, l in zip(range(self.rows), range(self.cols-1, -1, -1)):
            for j, k in zip(range(self.rows), range(self.cols-1, -1, -1)):
                if j < l:
                    self.matrix[i][j], self.matrix[k][l] = self.matrix[k][l], self.matrix[i][j]

        return self

    def transpose_by_main_line(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i > j:
                    self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        return self

    def transpose_by_vertical_line(self):
        for i in range(self.rows):
            for j, k in zip(range(self.cols), range(self.cols-1, -1, -1)):
                if j < k:
                    self.matrix[i][j], self.matrix[i][k] = self.matrix[i][k], self.matrix[i][j]

        return self

    def transpose_by_horizontal_line(self):
        for j in range(self.cols):
            for i, k in zip(range(self.rows), range(self.rows-1, -1, -1)):
                if i < k:
                    self.matrix[i][j], self.matrix[k][j] = self.matrix[k][j], self.matrix[i][j]

        return self

    def transposeMatrix(self, m):
        return list(map(list,zip(*m)))

    def getMatrixMinor(self, m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(self, m):
        #base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m,0,c))
        return determinant

    def getMatrixInverse(self, m):
        determinant = self.getMatrixDeternminant(m)
        #special case for 2x2 matrix:
        if len(m) == 2:
            return Matrix(matrix=[[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]])

        #find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return Matrix(matrix=cofactors)

    def __str__(self) -> str:
        self.show_matrix()
        return ''


def main():
    while True:
        choice = input(
            '1. Add matrices\n'
            '2. Multiply matrix by a constant\n'
            '3. Multiply matrices\n'
            '4. Transpose matrix\n'
            '5. Calculate a determinant\n'
            '6. Inverse matrix\n'
            '0. Exit\nYour choice: ')

        if choice == '1':
            matrix1 = Matrix.trans_from_str(Matrix())
            matrix2 = Matrix.trans_from_str(Matrix())
            print(matrix1.sum(matrix2))

        if choice == '2':
            factor = int(input('Enter your factor to mupltiply matrix: '))
            matrix1 = Matrix.trans_from_str(
                Matrix()).multiply_by_factor(factor).show_matrix()

        if choice == '3':
            matrix1 = Matrix.trans_from_str(Matrix())
            matrix2 = Matrix.trans_from_str(Matrix())
            print(matrix1.multiply_on_matrix(matrix2))

        if choice == '4':
            trans_type = input(
                '1. Main diagonal\n'
                '2. Side diagonal\n'
                '3. Vertical line\n'
                '4. Horizontal line\n'
                'Your choice: ')

            try:
                matrix1 = Matrix.trans_from_str(Matrix())
                if trans_type == '1':
                    matrix1.transpose_by_main_line()

                if trans_type == '2':
                    matrix1.transpose_by_side_line()

                if trans_type == '3':
                    matrix1.transpose_by_vertical_line()

                if trans_type == '4':
                    matrix1.transpose_by_vertical_line()

            finally:
                print(matrix1)

        if choice == '5':
            matrix1 = Matrix.trans_from_str(Matrix())
            print(matrix1.getMatrixDeternminant(matrix1.matrix))

        if choice == '6':
            matrix1 = Matrix.trans_from_str(Matrix())
            print(matrix1.getMatrixInverse(matrix1.matrix))
        if choice == '0':
            break


if __name__ == "__main__":
    main()
