import time, sys
def maximal_square(m, n, h, matrix, k):
    max_size = 0
    boundary = []
    
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m-i, n-j)+1):
                for f in range(i, i+size):
                    for l in range(j, j+size):
                        num_enclosed_plots = countEnclosedPlotsAndMinTreeRequirement(matrix, i, j, size)
                if num_enclosed_plots <= k:
                    if size > max_size:
                        boundary = [i, j, i+size-1, j+size-1]
                        max_size = size
    
    return boundary

def countEnclosedPlotsAndMinTreeRequirement(grid, i, j, s):
    # num_enclosed_plots, min_tree_requirement = 0, float('inf')
    num_enclosed_plots, min_tree_requirement = 0, 0
    for r in range(i, i+s):
        for c in range(j, j+s):
            if grid[r][c] < h:
                num_enclosed_plots += 1

    return num_enclosed_plots

# Read the first line of input and split it into three variables
m, n, h, k = map(int, input().split())

# Initialize an empty list to store the matrix
matrix = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# # Comparative Study ##########################################
# # open the file for reading
# with open(str(sys.argv[1]), 'r') as f:
    
#     # read the first line and extract the dimensions
#     dimensions = f.readline().split()
#     m = int(dimensions[0])
#     n = int(dimensions[1])
#     h = int(dimensions[2])
#     k = int(dimensions[3])
    
#    # initialize the matrix variable
#     matrix = [[0]*n for i in range(m)]
    
#     # read the remaining lines and populate the matrix variable
#     for i in range(m):
#         row = f.readline().split()
#         for j in range(n):
#             matrix[i][j] = int(row[j])

# ############################################################

# start_time = time.time()  # record the start time
# Call the maximal_square function
boundary = maximal_square(m, n, h, matrix, k)
# end_time = time.time()  # record the end time

for val in boundary:
    print(val+1, end= ' ')

# runtime = end_time - start_time  # calculate the runtime
# print()
# print(f"Runtime: {runtime:.4f} seconds")