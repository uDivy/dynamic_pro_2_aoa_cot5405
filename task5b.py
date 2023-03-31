def largest_square_area(p, h):
    m, n = len(p), len(p[0])
    # Step 1: Initialize DP matrix
    DP = [[0 for j in range(n)] for i in range(m)]
    
    # Step 2: Fill DP matrix using recurrence relation
    max_size = 0
    for i in range(0, m):
        for j in range(0, n):
            if p[i][j] < h:
                if i<m-1 and j<n-1:
                    if(p[i][j+1]>=h and p[i+1][j]>=h and p[i+1][j+1]>=h):
                        print("top left", i,j)
                        DP[i][j] = 1
                    elif(p[i][j-1]>=h and p[i+1][j]>=h and p[i+1][j-1]>=h):
                        print("top right",i,j)
                        DP[i][j] = 1
                    elif(p[i-1][j]>=h and p[i][j+1]>=h and p[i-1][j+1]>=h):
                        print("bottom left", i, j)
                        DP[i][j] = 1
                    elif(p[i-1][j-1]>=h and p[i][j-1]>=h and p[i-1][j]>=h):
                        DP[i][j] = 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
            else:
                DP[i][j] = 1 + min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1])
            max_size = max(max_size, DP[i][j])
    
    # Step 3: Find bounding indices of largest square-shaped area
    for i in range(0, m):
        for j in range(0, n):
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