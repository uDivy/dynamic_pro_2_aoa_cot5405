def maximal_square(m, n, h, matrix):
    max_size = 0
    boundary = []
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] >= h:
                size = 1
                is_square = True
                while i + size < m and j + size < n and is_square:
                    for k in range(j + size, j + size + 1):
                        if matrix[i][k] < h:
                            is_square = False
                            break
                    for k in range(j , j + size + 1):
                        if matrix[i + size][k] < h:
                            is_square = False
                            break
                    if is_square:
                        size += 1
                if max_size < size:
                    boundary = [i, j,i+size-1, j + size-1]
                    max_size = size

    
    return boundary

# Read the first line of input and split it into three variables
m, n, h = map(int, input().split())

# Initialize an empty list to store the matrix
matrix = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the maximal_square function
boundary = maximal_square(m, n, h, matrix)
for val in boundary:
    print(val+1,end=' ')