rows = int(input("Enter number of rows:\n"))
cols = int(input("Enter number of columns:\n"))
matrix = []



for i in range(rows):
    a = []
    for j in range(cols):
        a.append(-1*(i+1) + (j+1)*2)
    matrix.append(a)

print("\nThe matrix is:\n")

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end = " ")
    print()