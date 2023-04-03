def maximal_square(m, n, h, matrix):
    max_size = 0
    boundary = []
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] >= h:
                for size in range(1, min(m-i, n-j)+1):
                    is_square = True
                    for k in range(i, i+size):
                        for l in range(j, j+size):
                            if matrix[k][l] < h:
                                is_square = False
                                break
                        if not is_square:
                            break
                    if is_square:
                        if size > max_size:
                            boundary = [i, j, i+size-1, j+size-1]
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