#write a method to rotate the image by 90 degree. Do this in place
def rotate(matrix):
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i].reverse()

def rotate2(a):
    if len(a) == 0 or len(a) != len(a[0]):
        return False
    n = len(a)

    for layer in range(0, n // 2):
        first = layer
        last = n - 1 - first
        for i in range(first, last):
            offset = i - first
            top = a[first][i]
            bottom = a[last][last - offset]
            left = a[last - offset][first]
            right = a[i][last]

            # //left -> top
            a[first][i] = left

            # bottom ->left
            a[last - offset][first] = bottom

            # right -> bottom
            a[last][last - offset] = right

            # top ->right
            a[i][last] = top
    return a


if __name__ == '__main__':
    theArr = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [12, 14, 15, 16]]
    print(rotate(theArr))