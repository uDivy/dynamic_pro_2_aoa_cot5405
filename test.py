def find_max_square(matrix, k, h):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[[-1 for _ in range(k+1)] for _ in range(cols)] for _ in range(rows)]
    
    def find_max_square_helper(i, j, k, h):

        if i >= rows or j >= cols:
            return 0

        if dp[i][j][k] != -1:
            return dp[i][j][k]
        else:
            right = find_max_square_helper(i+1, j, k, h)
            below =  find_max_square_helper(i, j+1, k, h)
            diag = find_max_square_helper(i+1, j+1, k, h)
            dp[i][j][k] = 0
            if matrix[i][j] >= h:
                dp[i][j][k] = 1 + min(right, below, diag)
            else:
                print(i, j)
            
        return dp[i][j][k]
    
    max_size, start, end = 0, None, None
    for i in range(rows):
        for j in range(cols):
            for k_val in range(k+1):
                size = find_max_square_helper(i, j, k_val, h)
                if size > max_size:
                    max_size = size
                    start, end = (i,j), (i+size-1, j+size-1)
                    print(size, start, end, k_val)
                    
    return start, end

# Read the first line of input and split it into three variables
m, n, h, k = map(int, input().split())

# Initialize an empty list to store the matrix
matrix = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the maximal_square function
boundary = find_max_square(matrix, k, h)
print(boundary)