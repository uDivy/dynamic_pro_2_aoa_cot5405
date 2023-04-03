import time, sys
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

# # Read the first line of input and split it into three variables
# m, n, h = map(int, input().split())

# # Initialize an empty list to store the matrix
# p = []

# # Iterate over the remaining lines of input and append each row to the matrix
# for _ in range(m):
#     row = list(map(int, input().split()))
#     p.append(row)

# Comparative Study ##########################################
# open the file for reading
with open(str(sys.argv[1]), 'r') as f:
    
    # read the first line and extract the dimensions
    dimensions = f.readline().split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    h = int(dimensions[2])
    
   # initialize the matrix variable
    p = [[0]*n for i in range(m)]
    
    # read the remaining lines and populate the matrix variable
    for i in range(m):
        row = f.readline().split()
        for j in range(n):
            p[i][j] = int(row[j])

############################################################

start_time = time.time()  # record the start time
[a,b,c,d] = largest_square_area(p, h)
end_time = time.time()  # record the end time
print(a+1, b+1, c+1, d+1)
runtime = end_time - start_time  # calculate the runtime
print()
print(f"Runtime: {runtime:.4f} seconds")