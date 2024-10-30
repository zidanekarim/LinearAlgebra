import numpy as np

def print_matrix(matrix):
    print("\nThe matrix is:\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print()
    print("\n")


print("Matrix 1:\n ")
rows = int(input("Enter number of rows:\n"))
cols = int(input("Enter number of columns:\n"))
matrix1 = []
vals = input("Enter values separated:\n")
matrix1vals = [int(i) for i in vals.split()]


for i in range(rows):
    a = []
    for j in range(cols):
        a.append(matrix1vals.pop(0))
    matrix1.append(a)
print_matrix(matrix1)

print("Matrix 2:\n ")

matrix2 = []

rows = int(input("Enter number of rows:\n"))
cols = int(input("Enter number of columns:\n"))

vals = input("Enter values separated:\n")
matrix2vals = [int(i) for i in vals.split()]

for i in range(rows):
    a = []
    for j in range(cols):
        a.append(matrix2vals.pop(0))
    matrix2.append(a)
print_matrix(matrix2)
def mutliply_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2)





print(mutliply_matrix(matrix1, matrix2))