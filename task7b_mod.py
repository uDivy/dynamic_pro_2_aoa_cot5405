class ufa:
  def calculate(matrix, k, h):
    r_x,r_y,r_s = None,None,0
    hash_map = {}

    def find_count(i,j,d):
      if(i-d<0 or j-d<0):
        return float("inf")
      count = 0
      if(matrix[i][j-d]<h):
        count += 1
      if(matrix[i-d][j]<h):
        count += 1
      return count

    # Create a 3D array to store the intermediate results
    dp = [[[0] * (k+1) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
       for j in range(len(matrix[0])):
          if matrix[i][j] >= h:
             dp[i][j][0] = 1
             
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            for l in range(1, k+1):
              if(matrix[i][j]<h):
                  l -= 1
              d = 1
              ts = 1
              l -= find_count(i,j,d)
              

              while(l>=0):
                  temp = dp[i - 1][j - 1][l]
                  if (temp >= d):
                      ts += 1
                  d += 1
                  if (i - d < 0 or j - d < 0):
                      break
                  l -= find_count(i, j, d)
                  if l < 0:
                      break

              dp[i][j][l] = ts
              if(ts>r_s):
                  print(i, j, dp[i][j])
                  r_x,r_y,r_s = i,j,ts
              

    print(r_x+2-r_s, r_y+2-r_s, r_x+1, r_y+1)
  
# Read the first line of input and split it into three variables
m, n, h, k = map(int, input().split())

# Initialize an empty list to store the matrix
matrix = []

# Iterate over the remaining lines of input and append each row to the matrix
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the maximal_square function
ufa.calculate(matrix, k , h)