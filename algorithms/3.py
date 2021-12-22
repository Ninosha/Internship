from pprint import pprint

grid = []

n = 5

new_grid = [list(i) for i in grid]
grid_after_2 = []
for i in grid:
    i = "O" * len(i)
    grid_after_2.append(i)


# 3
def bomberman(n, grid):
    # creating list of lists
    new_grid = [list(i) for i in grid]
    # iteration in original grid to replace all chars with "O"
    for i in grid:
        i.replace(i, "O")
    # if it's the 2nd second returns grid with all the "O"
    if n % 3 == 2 or n == 2:
        # grid full of "O"-s
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


def printGrid(grid):
    for row in grid:
        print("".join(row))


r, c, n = [int(i) for i in input().strip().split()]
D = [['O' for i in range(c)] for j in range(r)]

G = []
for _ in range(r):
    G.append(list(input()))

S3 = [['.' for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if not ((j + 1 < c and G[i][j + 1] == 'O') or (j - 1 >= 0 and G[i][j - 1] == 'O') or (
                i - 1 >= 0 and G[i - 1][j] == 'O') or (i + 1 < r and G[i + 1][j] == 'O')):
            if (G[i][j] != 'O'): S3[i][j] = 'O'

S5 = [['.' for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        if not ((j + 1 < c and S3[i][j + 1] == 'O') or (j - 1 >= 0 and S3[i][j - 1] == 'O') or (
                i - 1 >= 0 and S3[i - 1][j] == 'O') or (i + 1 < r and S3[i + 1][j] == 'O')):
            if S3[i][j] != 'O': S5[i][j] = 'O'

if n % 2 == 0:
    printGrid(D)
elif n == 1:
    printGrid(G)
elif (n + 1) % 4 == 0:
    printGrid(S3)
else:
    printGrid(S5)
