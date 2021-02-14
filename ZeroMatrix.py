#write a algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

def zeroMatrix(arr):
    row = [False] * len(arr)
    col = [False] * len(arr[0])

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                row[i] = True
                col[j] = True
    # nullify row
    for i in range(len(row)):
        if row[i]:
            nullifyRow(arr, i)

    # nullify column
    for j in range(len(col)):
        if col[j]:
            nullifyCol(arr, j)

def nullifyRow(arr, row):
    for j in range(len(arr[0])):
        arr[row][j] = 0


def nullifyCol(arr, col):
    for i in range(len(arr)):
        arr[i][col] = 0

if __name__ == '__main__':
    theArr = [[1, 2, 4],
              [0, 6, 8],
              [9, 10, 0]]
    print(zeroMatrix(theArr))