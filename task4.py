def largest_square_area(p, h):
    # Step 1: Initialize DP matrix
    DP = [[0 for j in range(n)] for i in range(m)]
    zero = False
    max_size= 0

    # Step 2: Recursively set 
    for i in range(0, m):
        for j in range(0, n):
            for k in range(j+1, n):
                if DP[i][k] == 0:
                    if p[i][k] >= h:
                        if p[i][j] < h:
                            if k==j+1:                            
                                DP[i][k] = k - j + 1
                                zero = True
                        else:
                            DP[i][k] = k - j
                            zero = False
                    else:
                        DP[i][k] = DP[i][k-1]
                max_size = max(max_size, DP[i][j])

    # Step 3: Find bounding indices of largest square-shaped area
    for i in range(m):
        for j in range(n):
            if DP[i][j] != 0:
                if zero:
                    j -= 1
                    bottom = i+max_size
                    right = j+max_size
                else:
                    bottom = i+max_size-1
                    right = j+max_size-1
                return [i,j,bottom,right]
            else:
                return [0,0,1,1]

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