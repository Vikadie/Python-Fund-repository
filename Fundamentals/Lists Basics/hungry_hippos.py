rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

cols = len(matrix[0])
food_blocks = 0

def is_Safe(matrix, visited, row, col): # a finc to check if a given cell can be included in DFS()
    return (row >= 0 and row < rows and
            col >= 0 and col < cols and
            matrix[row][col] and not visited[row][col]) # return True if this cell in matrix=1 and it's not been visited

def DFS(row, col, visited): # the DFS function check the neighbour cells above, below and from both sides

    # arrays for neighbour cells to be checked (to be checked in tuples)
    row_num = [-1, 0, 0, 1]
    col_num = [0, -1, 1, 0]

    # mark the current cell as visited
    visited[row][col] = True

    for k in range(len(row_num)): # for k in range 4 neighbours
        if is_Safe(matrix, visited, row + row_num[k], col + col_num[k]):
            DFS(row + row_num[k], col + col_num[k], visited) # recursion to catch the whole island

# initializing bool 2d-array (size same as matrix) with all values set to False
visited = [[False for col in range(cols)]for row in range(rows)]

for row in range(rows):
    for col in range(cols):
        if visited[row][col] == False and matrix[row][col] == 1: # check if this cell has value 1 and is not visited yet
            DFS(row, col, visited) # call DFS to check all the neighbour cells
            food_blocks += 1

print(food_blocks)