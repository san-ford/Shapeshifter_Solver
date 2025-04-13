# place a piece on the board
def place(shape, grid, loc):
    for r in range(len(shape)):
        for c in range(len(shape[r])):
            if shape[r][c]:
                grid[r+loc[0]][c+loc[1]] = not grid[r+loc[0]][c+loc[1]]
    return grid


# find all possible places a piece can be placed
def findStartPoints(grid, shape):
    r = len(grid) - len(shape)
    c = len(grid[0]) - len(shape[0])

    starting_points = []
    for i in range(r+1):
        for j in range(c+1):
            starting_points.append((i, j))
    return starting_points


# depth first search to find all combinations of where pieces can be placed
# end when first solution found, or none
def dfs(grid, shapes, i, solution):
    # if at the end, check board
    if i >= len(shapes):
        for r in grid:
            for c in r:
                if not c:
                    return False
        return True

    # iterate through each start location for each piece
    starts = findStartPoints(grid, shapes[i])
    for start in starts:
        # place piece
        grid = place(shapes[i], grid, start)
        # add to memo and move to next shape
        solution.append(start)
        if dfs(grid, shapes, i+1, solution):
            # reset board
            grid = place(shapes[i], grid, start)
            if not i:
                print("First solution:", solution)
                return
            return True
        # reset board and solution
        solution.pop()
        grid = place(shapes[i], grid, start)
    if not i:
        # solution not found
        print("No solution found.")
    return False


# set up board and shapes (different for each level)
board = [[True, False, True],
         [False, True, True],
         [False, False, True],
         [True, False, True]]

shapes = [
    [[True, False, False],
     [True, True, False],
     [False, True, True]],

    [[True, True, True],
     [False, True, False],
     [True, True, True]],

    [[False, True, True],
     [True, True, True]],

    [[False, True, True],
     [True, True, True]],

    [[True, True],
     [True, True],
     [True, True]],

    [[True, False, False],
     [True, True, False],
     [False, True, True]],

    [[True, True, True],
     [True, False, True],
     [True, True, True]],

    [[True, True, True],
     [True, False, True],
     [True, True, True]],

    [[True, False],
     [True, True],
     [False, True]],

    [[True, True],
     [True, False]],

    [[True, False],
     [True, True],
     [False, True]],

    [[True, True, True],
     [False, True, False],
     [True, True, True]],

    [[True, False],
     [True, True],
     [False, True]],

    [[True, True, True],
     [False, True, False]],

    [[True, False, False],
     [True, True, False],
     [False, True, True]],

    [[True, True, True]]
]

# find solution for given board
dfs(board, shapes, 0, [])
