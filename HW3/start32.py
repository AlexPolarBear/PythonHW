from matrix32 import Matrix


matrix1 = Matrix(10, 10)
matrix2 = Matrix(10, 10)

matrix1.save_to_file('HW3/artifacts/3.2/matrix1.txt')
matrix2.save_to_file('HW3/artifacts/3.2/matrix2.txt')

sum_res = matrix1 + matrix2
sum_res.save_to_file('HW3/artifacts/3.2/matrix+.txt')

sub_res = matrix1 - matrix2
sub_res.save_to_file('HW3/artifacts/3.2/matrix-.txt')

mul_res = matrix1 * matrix2
mul_res.save_to_file('HW3/artifacts/3.2/matrix*.txt')

div_res = matrix1 // sum_res  # чтобы постараться избежать деления на нуль
div_res.save_to_file('HW3/artifacts/3.2/matrix%.txt')

print(matrix1)
