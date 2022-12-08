with open("input.txt") as data:
    data = [x.strip() for x in data.readlines()]

n_col = len(data[0])
n_row = len(data)
n_edge_visible = 4*n_row - 4
n_interior_visible = 0

# index strategy: data[row][col]

visible_trees = set()

# solution: trace row-wise and col-wise lasers, add visible trees to a set
for r in range(n_row):
    # trace horizontally from left -> right
    max_height = -1
    for c in range(n_col):
        is_visible = False
        peak = int(data[r][c])
        if peak > max_height:
            max_height = peak
            visible_trees.add((r, c))
    # trace horizontally from right -> left
    max_height = -1
    for c in reversed(range(n_col)):
        is_visible = False
        peak = int(data[r][c])
        if peak > max_height:
            max_height = peak
            visible_trees.add((r, c))

for c in range(n_col):
    # trace vertically from top -> bottom
    max_height = -1
    for r in range(n_row):
        is_visible = False
        peak = int(data[r][c])
        if peak > max_height:
            max_height = peak
            visible_trees.add((r, c))
    # trace vertically from bottom -> top
    max_height = -1
    for r in reversed(range(n_row)):
        is_visible = False
        peak = int(data[r][c])
        if peak > max_height:
            max_height = peak
            visible_trees.add((r, c))

# part 1
print(len(visible_trees))

def scenic_score(r, c, forest):
    peak = int(forest[r][c])
    n_col = len(forest[0])
    n_row = len(forest)
    up, right, down, left = 0, 0, 0, 0
    # calculate up
    for i in reversed(range(r)):
        up += 1
        view_peak = int(forest[i][c])
        if view_peak >= peak:
            break
    # calculate right
    for i in range(c + 1, n_col):
        right += 1
        view_peak = int(forest[r][i])
        if view_peak >= peak:
            break   
    # calculate down
    for i in range(r + 1, n_row):
        down += 1
        view_peak = int(forest[i][c])
        if view_peak >= peak:
            break 
    # calculate right
    for i in reversed(range(c)):
        left += 1
        view_peak = int(forest[r][i])
        if view_peak >= peak:
            break  
    return up * right * down * left

max_score = 0
for r in range(n_row):
    for c in range(n_col):
        score = scenic_score(r, c, data)
        if score > max_score:
            max_score = score

# part 2
print(max_score)

