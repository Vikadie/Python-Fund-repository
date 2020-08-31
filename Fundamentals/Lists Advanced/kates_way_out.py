import sys

rows_in_maze = int(input())

def check(matrix, i, j, is_visited):
    if ((matrix[i][j] == ' '
            and i >= 0 and i < rows_in_maze
            and j >= 0 and j < len(matrix[0])
            and not is_visited[i][j])):
        return 1
    return 0

#
# def DFS(start_i, start_j, is_visited, moves):
#     """the DFS function check the neighbour cells above, below and from both sides and count the moves for only those
#      that are free to move"""
#
#     # arrays for neighbour cells to be checked (to be checked in tuples)
#     i_num = [-1, 0, 0, 1]
#     j_num = [0, -1, 1, 0]
#     i = start_i
#     j = start_j
#
#     kate_is_out = False
#     while True:
#         is_visited[i][j] = True
#         found = 0
#         if (i == 0 or i == rows_in_maze - 1) or (j == 0 or j == len(matrix[0]) - 1):
#             kate_is_out = True
#             moves += 1
#             break
#         for k in range(len(i_num)):
#             if check(matrix, i + i_num[k], j + j_num[k], is_visited):
#                 moves += 1
#                 i = i + i_num[k]
#                 j = j + j_num[k]
#                 found = 1
#                 break
#         if k == 3 and not found:
#             break
#     moves_1 = 0
#     i = start_i
#     j = start_j
#
#     while True:
#         found = 0
#         is_visited[i][j] = True
#         if (i == 0 or i == rows_in_maze - 1) or (j == 0 or j == len(matrix[0]) - 1):
#             kate_is_out = True
#             moves_1 += 1
#             break
#         for l in range(len(i_num) - 1, -1, -1):
#             if check(matrix, i + i_num[l], j + j_num[l], is_visited):
#                 moves_1 += 1
#                 i = i + i_num[l]
#                 j = j + j_num[k]
#                 found = 1
#                 break
#         if k == 3 and not found:
#             break
#
#     if moves_1 < moves and found == 1:
#         moves = moves_1
#
#     return kate_is_out, moves

def solveMaze(matrix, i, j, is_visited, moves):

    if solveMazeUtil(matrix, i, j, is_visited, moves) == False:
        print("Solution doesn't exist")
        return False

    moves += 1
    return True


# A recursive utility function to solve Maze problem
def solveMazeUtil(matrix, i, j, is_visited, moves):
    # if (i, j is goal) return True
    if (i == 0 or i == rows_in_maze - 1) or (j == 0 or j == len(matrix[0]) - 1):
        kate_is_out = True
        moves += 1
        return True

    # Check if matix[i][j] is valid
    if check(matrix, i, j, is_visited) == True:
        # mark x, y as part of solution path
        is_visited[i][j] = 1

        # Move forward in x direction
        if solveMazeUtil(matrix, i + 1, j, is_visited, moves) == True:
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMazeUtil(matrix, i, j + 1, is_visited, moves) == True:
            return True

        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        is_visited[i][j] = 'X'
        return False

i, j = None, None
matrix = []
for r in range(rows_in_maze):
    row = list(input())
    matrix.append(row)
    if r > 0 and len(matrix[r-1]) > len(row):
        while len(matrix[r-1]) > len(row):
            matrix[r].append(" ")
    elif r > 0 and len(row) > len(matrix[r - 1]):
        while len(row) > len(matrix[r - 1]):
            matrix[r - 1].append((" "))
    if 'k' in row:
        start_i = r
        start_j = row.index('k')

kate_is_out = False
moves = 0
i = start_i
j = start_j

if (i is not None and j is not None) and \
        (all(1 if q == '#' else 0 for q in matrix[0]) and all(1 if q == '#' else 0 for q in matrix[-1]) and
         all([1 if (matrix[p][0] == '#' and matrix[p][-1] == '#') else 0 for p in range(1, len(matrix) - 1)])):
    kate_is_out = False # print("Kate cannot get out")
else:
    is_visited = [[False for col in range(len(matrix[0]))] for row in range(rows_in_maze)]

    if (i == 0 or i == rows_in_maze - 1) or (j == 0 or j == len(matrix[0]) - 1):
        kate_is_out = True
        moves += 1
    else:
        kate_is_out, moves = solveMaze(matrix, start_i, start_j, is_visited, moves)

if kate_is_out:
    print(f"Kate got out in {moves} moves")
else:
    print("Kate cannot get out")