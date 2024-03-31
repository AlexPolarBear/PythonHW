import hashlib
import numpy as np


class Matrix:
    def __init__(self, rows = float('inf'), columns = float('inf')):
        if rows == float('inf') or columns == float('inf'):
            raise ValueError("Матрицы не могут быть пустыми или бесконечными.")
        self.rows = rows
        self.columns = columns
        self.data = np.random.randint(0, 10, (rows, columns))

    def __add__(self, dif):
        if not isinstance(dif, Matrix):
            raise ValueError("Что-то не так с твоей матрицей.")
        if self.rows != dif.rows or self.columns != dif.columns:
            raise ValueError("Фу таким быть, складывай матрицы одного размера!")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for ii in range(self.columns):
                result.data[i][ii] = self.data[i][ii] + dif.data[i][ii]
        return result
    
    def __mul__(self, dif):
        if not isinstance(dif, Matrix):
            raise ValueError("Что-то не так с твоей матрицей.")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] * dif.data[i][j]
        return result

    def __matmul__(self, dif):
        if not isinstance(dif, Matrix):
            raise ValueError("Что-то не так с твоей матрицей.")
        if self.columns != dif.rows:
            raise ValueError("Количество строк первой матрице не равно количеству столбцов второй.")
        
        result = Matrix(self.rows, dif.columns)
        for i in range(self.rows):
            for ii in range(dif.columns):
                for iii in range(self.columns):
                    result.data[i][ii] += self.data[i][iii] * dif.data[iii][ii]
        return result

matrix = Matrix(10, 10)
print(hashlib.sha1(matrix.data).hexdigest())