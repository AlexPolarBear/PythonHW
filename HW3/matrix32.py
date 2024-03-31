import numpy as np


class Arifmetic:
    def __add__(self, dif):
        if not isinstance(dif, Matrix):
            raise ValueError("Что-то не так с твоей матрицей.")
        if self.rows != dif._rows or self.columns != dif._columns:
            raise ValueError("Фу таким быть, складывай матрицы одного размера!")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for ii in range(self.columns):
                result.data[i][ii] = self.data[i][ii] + dif.data[i][ii]
        return result
    
    def __sub__(self, dif):
        if self.rows != dif.rows or self.columns != dif.columns:
            raise ValueError("Матрицы должны быть одного размера.")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for ii in range(self.columns):
                result.data[i][ii] = self.data[i][ii] - dif.data[i][ii]
        return result
    
    def __mul__(self, dif):
        if not isinstance(dif, Matrix):
            raise ValueError("Что-то не так с твоей матрицей.")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] * dif.data[i][j]
        return result
    
    def __floordiv__(self, dif):
        if self.rows != dif.rows or self.columns != dif.columns:
            raise ValueError("Матрицы должны быть одного размера.")
        for i in range(self.rows):
            for j in range(self.columns):
                if dif.data[i][j] == 0:
                    raise ValueError("Деление на нуль")
        
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] // dif.data[i][j]
        return result


class SaveFile:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.data))


class Display:
    def __str__(self):
        matrix = [' '.join(map(str, row)) for row in self.data]
        result = '\n'.join(matrix)
        return result


class Accessors:
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, value):
        self._rows = value
        self.data = np.random.randint(0, 10, (self._rows, self._columns))

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value
        self.data = np.random.randint(0, 10, (self._rows, self._columns))


class Matrix(Arifmetic, SaveFile, Display, Accessors):
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self.data = np.random.randint(0, 10, (rows, columns))
