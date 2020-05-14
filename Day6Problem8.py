def spiral(List, startRow, endRow, startColumn, endColumn):
    if startRow == endRow:
        for i in range(startColumn, endColumn):
            print(List[startRow][i], end = " ")
        print(List[startRow][endColumn], end = " ")
        return
    if startColumn == endColumn:
        for i in range(startRow, endRow):
            print(List[i][startColumn], end = " ")
        print(List[startRow][endColumn], end = " ")
        return
    for i in range(startColumn, endColumn):
        print(List[startRow][i], end = " ")
    for i in range(startRow, endRow):
        print(List[i][endColumn], end = " ")
    for i in range(endColumn, startColumn, -1):
        print(List[endRow][i], end = " ")
    for i in range(endRow, startRow,-1):
        print(List[i][startColumn], end = " ")
    spiral(List, startRow + 1, endRow - 1, startColumn + 1, endColumn - 1)

m = int(input("Enter the number of rows in the matrix: "))
n = int(input("Enter the number of columns in the matrix: "))
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(int(input("Enter the element in matrix at (" + str(i+1) + ", " + str(j+1) + "): ")))
    a.append(b)
print("The element of matrix in spiral form are as follows: ")
spiral(a, 0, m-1, 0, n-1)
