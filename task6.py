def findMaximalSquare(grid, k, h):
    m, n = len(grid), len(grid[0])
    max_size, top_left, bottom_right = 0, None, None
    
    # check all possible squares with top-left corner (i, j)
    for i in range(m):
        for j in range(n):
            # check squares with size s
            for s in range(1, min(m-i+1, n-j+1)):
                # check if the square is valid (at most k enclosed plots have a minimum tree requirement less than h)
                num_enclosed_plots, min_tree_requirement = countEnclosedPlotsAndMinTreeRequirement(grid, i, j, s)
                if num_enclosed_plots <= k and min_tree_requirement < h:
                    # update maximum square found so far
                    if s > max_size:
                        max_size = s
                        top_left = (i, j)
                        bottom_right = (i+s-1, j+s-1)
    
    return top_left, bottom_right
    

def countEnclosedPlotsAndMinTreeRequirement(grid, i, j, s):
    num_enclosed_plots, min_tree_requirement = 0, float('inf')
    for r in range(i, i+s):
        for c in range(j, j+s):
            if grid[r][c] < h:
                num_enclosed_plots += 1
                # check if this plot has lower tree requirement than the current minimum
                if r == i or c == j:
                    min_tree_requirement = min(min_tree_requirement, 0)
                else:
                    min_tree_requirement = min(min_tree_requirement, grid[r-1][c-1], grid[r-1][c], grid[r][c-1])
            else:
                # reset minimum tree requirement since this plot is not enclosed
                min_tree_requirement = 0
    
    return num_enclosed_plots, min_tree_requirement

# Read the first line of input and split it into three variables
m, n, h, k = map(int, input().split())

# Initialize an empty list to store the matrix
matrix = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the maximal_square function
boundary = findMaximalSquare(matrix, k, h)
print(boundary)