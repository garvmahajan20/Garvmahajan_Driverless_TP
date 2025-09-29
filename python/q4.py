row1=int(input("rows of mat1"))
col1=int(input("cols of mat1"))
matrix1=[]
print("entries row wise")
for i in range(row1):
    rows1=[]
    for j in range(col1):
        rows1.append(int(input()))
    matrix1.append(rows1)
print("the matrix is")
for i in range(row1):
    for j in range(col1):
        print(matrix1[i][j],end=" ")
    print()
row2=int(input("rows of mat2"))
col2=int(input("cols of mat2"))
matrix2=[]
print("entries row wise")
for i in range(row2):
    rows2=[]
    for j in range(col2):
        rows2.append(int(input()))
    matrix2.append(rows2)
print("the matrix is")
for i in range(row2):
    for j in range(col2):
        print(matrix2[i][j],end=" ")
    print()
if col1!=row2:
    print("the matrices cannot be multiplied")
elif col1==row2:
    matrix=[[0 for _ in range(col2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            s=0
            for k in range(col1):
                s+=matrix1[i][k]*matrix2[k][j]
                matrix[i][j]=s
    print("the multiplied matrix is")
    for i in range(row1):
        for j in range(col2):
            print(matrix[i][j],end=" ")
        print()