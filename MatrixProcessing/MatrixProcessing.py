import random
from warnings import showwarning

class Matrix:
    def __init__(self, rows=None, cols=None, matrix = []) -> None:
        if matrix:
            self.matrix = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])
        elif rows and cols:
            self.matrix = []
            self.rows = rows
            self.cols = cols
        else:
            self.matrix = []
            self.rows = 0
            self.cols = 0
            return

        for row in range(self.rows):
            self.matrix.append([])
            for col in range(self.cols):
                self.matrix[-1].append(random.randint(-10,11))


    def sum(self, matrix2):
        if self.rows != matrix2.rows\
            and self.cols != matrix2.cols:
                print('ERROR: cant sum different shape matrix')
        
        new_matrix = []

        for i in range(self.rows):
            new_matrix.append([])
            for j in range(self.cols):
                new_matrix[-1].append((self.matrix[i][j]) + (matrix2.matrix[i][j]))

        return Matrix(matrix=new_matrix)


    def show_matrix(self):
        print('Printing matrix')
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.matrix[i][j], end='\t')
            print('')

        return self


    def trans_from_str(self):
        self.rows, self.cols = [int(x) for x in input('Size(rows, cols):').split()]
        
        for i in range(self.rows):
            self.matrix.append([int(x) for x in input(f'Enter row number {i+1}: ').split()])

        return self


    def mupltiply(self, factor):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] *= factor

        return self

    def __str__(self) -> str:
        self.show_matrix()
        return ''


def main():
    matrix1 = Matrix.trans_from_str(Matrix()).show_matrix()
    matrix1.mupltiply(2).show_matrix()


if __name__ == "__main__":
    main()