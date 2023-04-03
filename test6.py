def findMaximalSquare(grid, k, h):
    m, n = len(grid), len(grid[0])
    max_size, boundary = 0, []

    # check all possible squares with top-left corner (i, j)
    for i in range(m):
        for j in range(n):
            # check squares with size s
            for s in range(1, min(m-i+1, n-j+1)):
                # check if the square is valid (at most k enclosed plots have a minimum tree requirement less than h)
                num_enclosed_plots = countEnclosedPlotsAndMinTreeRequirement(grid, i, j, s)               
                if num_enclosed_plots <= k:
                    # update maximum square found so far
                    if s > max_size:
                        max_size = s
                        boundary = [i, j, i+s-1, j+s-1]

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
boundary = findMaximalSquare(matrix, k, h)
for val in boundary:
    print(val+1, end= ' ')