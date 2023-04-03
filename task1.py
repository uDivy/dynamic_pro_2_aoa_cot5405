import time, sys
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

# Comparative Study ##########################################
# open the file for reading
# with open(str(sys.argv[1]), 'r') as f:
    
#     # read the first line and extract the dimensions
#     dimensions = f.readline().split()
#     m = int(dimensions[0])
#     n = int(dimensions[1])
#     h = int(dimensions[2])
    
#    # initialize the matrix variable
#     matrix = [[0]*n for i in range(m)]
    
#     # read the remaining lines and populate the matrix variable
#     for i in range(m):
#         row = f.readline().split()
#         for j in range(n):
#             matrix[i][j] = int(row[j])

# ############################################################


start_time = time.time()  # record the start time
# Call the maximal_square function
boundary = maximal_square(m, n, h, matrix)
end_time = time.time()  # record the end time
for val in boundary:
    print(val+1,end=' ')
runtime = end_time - start_time  # calculate the runtime
# print(f"Runtime: {runtime:.4f} seconds")