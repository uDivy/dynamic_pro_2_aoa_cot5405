def find_max_square(matrix, k, h):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[[-1 for _ in range(k+1)] for _ in range(cols)] for _ in range(rows)]
    
    def find_max_square_helper(i, j, k, h, cnt):
        if i >= rows or j >= cols or cnt > k:
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        
        if matrix[i][j] >= h:
            size = 1 + min(find_max_square_helper(i+1, j, k, h, cnt), 
                        find_max_square_helper(i, j+1, k, h, cnt),
                        find_max_square_helper(i+1, j+1, k, h, cnt))
        else:
            cnt += 1
            size = 1 + min(find_max_square_helper(i+1, j, k, h, cnt), 
                        find_max_square_helper(i, j+1, k, h, cnt),
                        find_max_square_helper(i+1, j+1, k, h, cnt))

        dp[i][j][k] = size
        return size
    
    max_size, start, end = 0, None, None
    for i in range(rows):
        for j in range(cols):
            for k_val in range(k+1):
                size = find_max_square_helper(i, j, k_val, h, 0)
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