def largest_square_area(p, h):
    DP = [[0 for j in range(n)] for i in range(m)]
    max_size = 0

    def helper(i, j):
        if i < 0 or j < 0:
            return 0
        if DP[i][j] != 0:
            return DP[i][j]
        if p[i][j] < h:
            if i<m-1 and j<n-1:
                if(p[i][j+1]>=h and p[i+1][j]>=h and p[i+1][j+1]>=h):
                    DP[i][j] = 1
                elif(p[i][j-1]>=h and p[i+1][j]>=h and p[i+1][j-1]>=h):
                    DP[i][j] = 1
                elif(p[i-1][j]>=h and p[i][j+1]>=h and p[i-1][j+1]>=h):
                    DP[i][j] = 1
                elif(p[i-1][j-1]>=h and p[i][j-1]>=h and p[i-1][j]>=h):
                    DP[i][j] = 1 + min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1))
            else:
                DP[i][j] = 1 + min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1))
        else:
            DP[i][j] = 1 + min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1))
        nonlocal max_size
        max_size = max(max_size, DP[i][j])
        return DP[i][j]

    for i in range(m):
        for j in range(n):
            helper(i, j)

    for i in range(0,m):
        for j in range(0,n):
            if DP[i][j] == max_size:
                row_index = i - max_size + 1
                col_index = j - max_size + 1
                return (row_index, col_index, i, j)

# Read the first line of input and split it into three variables
m, n, h = map(int, input().split())

# Initialize an empty list to store the matrix
p = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    p.append(row)

[a,b,c,d] = largest_square_area(p, h)

print(a+1, b+1, c+1, d+1)