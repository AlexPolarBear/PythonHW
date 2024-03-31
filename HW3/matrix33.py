import numpy as np
from hashlib import md5


class MatrixHashAndCache:
    def __init__(self):
        self._cache = {}

    def __hash__(self, data):
        """
        Складывает элементы каждой строки и столбца,
        затем вычисляет MD5-хеш суммы.
        """
        row_sums = np.sum(data, axis=1)
        col_sums = np.sum(data, axis=0)
        sum_of_sums = row_sums.sum() + col_sums.sum()
        hash_value = md5(str(sum_of_sums).encode()).hexdigest()
        return int(hash_value, 16)

    def get_cache(self, matrix1, matrix2):
        """
        Возвращает произведение матриц, если оно уже было вычислено и закешировано.
        Иначе вычисляет произведение и сохраняет его в кеш.
        """
        hash_value = self.__hash__((matrix1, matrix2))
        if hash_value in self._cache:
            return self._cache[hash_value]
        else:
            product = matrix1 @ matrix2
            self._cache[hash_value] = product
            return product