def maximal_square(m, n, h, matrix):
    max_size = 0
    boundary = []
    dp = [0] * n
    
    for i in range(m):
        prev = 0
        for j in range(n):
            if matrix[i][j] >= h:
                temp = dp[j]
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(prev, dp[j], dp[j-1]) + 1
                prev = temp
                if dp[j] > max_size:
                    max_size = dp[j]
                    boundary = [(i-max_size+1, j-max_size+1), (i, j)]
            else:
                dp[j] = 0
                
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
print(boundary[0], boundary[1])