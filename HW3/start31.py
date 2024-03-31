import numpy as np
from matrix31 import Matrix


np.random.seed(0)

matrix1 = Matrix(10, 10)
matrix2 = Matrix(10, 10)

result = matrix1 + matrix2
with open("HW3/artifacts/3.1/matrix+.txt", "w") as file:
    string = str(matrix1.data) + "\n" + "+".center(23) + "\n"
    string += str(matrix2.data) + "\n" + "=".center(23) + "\n" + str(result.data)
    file.write(str(string))

result = matrix1 * matrix2
with open("HW3/artifacts/3.1/matrix*.txt", "w") as file:
    string = str(matrix1.data) + "\n" + "*".center(23) + "\n"
    string += str(matrix2.data) + "\n" + "=".center(23) + "\n" + str(result.data)
    file.write(str(string))

result = matrix1 @ matrix2
with open("HW3/artifacts/3.1/matrix@.txt", "w") as file:
    string = str(matrix1.data) + "\n" + "@".center(23) + "\n"
    string += str(matrix2.data) + "\n" + "=".center(23) + "\n" + str(result.data)
    file.write(str(string))
