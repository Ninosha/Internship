from pprint import pprint

grid = [".......",
"...O.O.",
"....O..",
"..O....",
"OO...OO",
"OO.O..."]

n = 5

new_grid = [list(i) for i in grid]
grid_after_2 = []
for i in grid:
    i = "O" * len(i)
    grid_after_2.append(i)


#
# print(grid_after_2)
# print(grid)


# 3
def bomberman(n, grid):
    new_grid = [list(i) for i in grid]
    for i in grid:
        i.replace(i, "O")
    if n % 3 == 2 or n == 2:
        grid_after_2 = []
        for i in grid:
            i = "O" * len(i)
            grid_after_2.append(i)
        return grid_after_2
    else:
        while n >= 3:
            for i in range(len(new_grid)):
                for j in range(len(new_grid[i])):
                    if new_grid[i][j] == ".":
                        new_grid[i][j] = "O"
                    else:
                        new_grid[i][j] = "B"
            for i in range(len(new_grid)):
                for j in range(len(new_grid[i])):
                    if new_grid[i][j] == "B":
                        new_grid[i][j] = "."
                        if j - 1 >= 0 and new_grid[i][j - 1] == "O":
                            new_grid[i][j - 1] = "."
                        if j + 1 < len(new_grid[i]) and new_grid[i][j + 1] == "O":
                            new_grid[i][j + 1] = "."
                        if i - 1 >= 0 and new_grid[i - 1][j] == "O":
                            new_grid[i - 1][j] = "."
                        if i + 1 < len(new_grid) and new_grid[i + 1][j] == "O":
                            new_grid[i + 1][j] = "."
            n -= 3
        return ["".join(i) for i in new_grid]


pprint(bomberman(n, grid))
