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

# Call the maximal_square function
boundary = maximal_square(m, n, h, matrix, k)
for val in boundary:
    print(val+1, end= ' ')