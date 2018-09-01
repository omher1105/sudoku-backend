import random
from datetime import datetime
from random import randint

from apps.sudoku.models import SudokuGenerate, SudokuDetail

SIZE = 9
matrix = [[0 for i in range(9)] for j in range(9)]


class SudokuUtils(object):

    @classmethod
    def init_sudoku(cls, data):
        cls.solucion_sudoku()
        matriz = list(matrix)
        random.shuffle(matriz)
        save = cls._save_sudoku_details(data=data, matriz=matriz)
        return save

    @classmethod
    def sudoku_status(cls, pk):
        queryset = SudokuDetail.objects.get(id=pk)
        queryset['state'] = 2 if queryset['state'] == 1 else 1
        queryset.save()
        return queryset

    @classmethod
    def _save_sudoku_details(cls, data, matriz):
        detail = {}
        sudoku_generate = {}
        detail['id_sudoku'] = sudoku_generate['id']
        detail['desc'] = data['name']
        detail['aud_user'] = ''
        detail['state'] = 1
        detail['aud_fecha_ini'] = datetime.now()
        detail['aud_fecha_fin'] = datetime.now()
        response = SudokuDetail.objects.create(detail)
        return response

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
