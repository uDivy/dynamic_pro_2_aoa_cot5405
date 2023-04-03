# open the file for reading
with open('filename.txt', 'r') as f:
    
    # read the first line and extract the dimensions
    dimensions = f.readline().split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    h = int(dimensions[2])
    
   # initialize the matrix variable
    matrix = [[0]*n for i in range(m)]
    print(matrix)
    
    # read the remaining lines and populate the matrix variable
    for i in range(m):
        row = f.readline().split()
        for j in range(n):
            matrix[i][j] = int(row[j])
    print(m, n, h, end=" ")
    print(matrix)