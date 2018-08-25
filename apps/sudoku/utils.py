SIZE = 9
matrix = [
    [6, 5, 0, 8, 7, 3, 0, 9, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 8],
    [9, 8, 0, 1, 0, 4, 3, 5, 7],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [5, 7, 8, 3, 0, 1, 0, 2, 6],
    [2, 0, 0, 0, 4, 8, 9, 0, 0],
    [0, 9, 0, 6, 2, 5, 0, 8, 1]]


class SudokuUtils(object):

    @classmethod
    def init_sudoku(cls):
        cls.solucion_sudoku()
        return matrix

    # funcion para imprimir
    @classmethod
    def imprimir_sudoku(cls):
        for i in matrix:
            print(i)

    # funcion para asignar un numero
    @classmethod
    def asignar_numero(cls, row, col):
        num_unassign = 0
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                # cell is unassigned
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    num_unassign = 1
                    a = [row, col, num_unassign]
                    return a
        a = [-1, -1, num_unassign]
        return a

    # validar
    @classmethod
    def validar_sudoku(cls, n, r, c):
        # verificar columna
        for i in range(0, SIZE):
            if matrix[r][i] == n:
                return False
        # verificar fila
        for i in range(0, SIZE):
            if matrix[i][c] == n:
                return False
        row_start = (r // 3) * 3
        col_start = (c // 3) * 3
        # verifica matrix
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if matrix[i][j] == n:
                    return False
        return True

    # resolucion de sudoku
    @classmethod
    def solucion_sudoku(cls):
        row = 0
        col = 0
        a = cls.asignar_numero(row, col)
        if a[2] == 0:
            return True
        row = a[0]
        col = a[1]
        # numero entre 1 y 9
        for i in range(1, 10):
            if cls.validar_sudoku(i, row, col):
                matrix[row][col] = i
                # backtracking
                if cls.solucion_sudoku():
                    return True
                matrix[row][col] = 0
        return False
