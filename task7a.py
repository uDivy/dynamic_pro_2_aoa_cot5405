import time, sys
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


    def find(i,j,k):

      if(hash_map.get((i,j,k))!=None):
          return hash_map.get((i,j,k))

      nonlocal r_x,r_y,r_s
      start = k
      ts = 0

      if(i>=0 and j>=0 and (matrix[i][j] >=h or (matrix[i][j]<h and k>0))):

        if(matrix[i][j]<h):
            k -= 1

        d = 1
        ts = 1

        k -= find_count(i,j,d)
        while(k>=0):
          temp = find(i-1,j-1,k)
          if(temp >= d):
            ts += 1
          d += 1
          k -= find_count(i,j,d)

      if(ts>r_s):
        r_x,r_y,r_s = i,j,ts

      hash_map[(i,j,start)] = ts
      return ts

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            find(i,j,k)

    print(r_x+2-r_s, r_y+2-r_s, r_x+1, r_y+1)

# # Read the first line of input and split it into three variables
# m, n, h, k = map(int, input().split())

# # Initialize an empty list to store the matrix
# matrix = []

# # Iterate over the remaining lines of input and append each row to the matrix
# for _ in range(m):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# Comparative Study ##########################################
# open the file for reading
with open(str(sys.argv[1]), 'r') as f:
    
    # read the first line and extract the dimensions
    dimensions = f.readline().split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    h = int(dimensions[2])
    k = int(dimensions[3])
    
   # initialize the matrix variable
    matrix = [[0]*n for i in range(m)]
    
    # read the remaining lines and populate the matrix variable
    for i in range(m):
        row = f.readline().split()
        for j in range(n):
            matrix[i][j] = int(row[j])

############################################################
start_time = time.time()  # record the start time
# Call the maximal_square function
ufa.calculate(matrix, k , h)
end_time = time.time()  # record the end time

runtime = end_time - start_time  # calculate the runtime
print()
print(f"Runtime: {runtime:.4f} seconds")