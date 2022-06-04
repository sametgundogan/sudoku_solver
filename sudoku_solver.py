
grid = [[2, '_', '_', 6, '_', '_', 1, 9, 7],
        ['_', 8, '_', '_', 1, '_', '_', 4, 2],
        [9, '_', '_', '_', '_', 7, '_', '_', '_'],
        ['_', 4, '_', '_', '_', '_', '_', '_', 6],
        [7, '_', 6, '_', '_', 9, '_', '_', '_'],
        [8, 9, '_', '_', '_', '_', 4, '_', '_'],
        ['_', 3, '_', '_', 6, '_', '_', 1, '_'],
        [1, '_', '_', '_', '_', 8, '_', '_', '_'],
        [4, 7, '_', 1, 3, 2, '_', 8, '_']]


def solver(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "_":
                row_set = set(grid[i])
                col_set = set([grid[x][j] for x in range(9)])

                sec_row = i // 3
                sec_col = j // 3
                sec_set = set()

                for k in range(3):
                    for m in range(3):
                        sec_set.add(grid[sec_row*3 + k][sec_col*3 + m])

                attempt = set(range(1, 10))
                attempt = ((attempt - row_set) - col_set) - sec_set

                if len(attempt) == 1:
                    a = attempt.pop()
                    grid[i][j] = a
    for i in grid:
        if '_' in i:
            solver(grid)

    return grid


def gridprint(grid):
    for i in range(len(grid) + 1):
        if i % 3 == 0:
            print(" -" * (len((grid[0])) + 7))
        if i == 9:
            break
        for j in range(len(grid[i]) + 1):
            if (j) % 3 == 0:
                print(" | ", end=" ")
            if j == 9:
                break
            print(grid[i][j], end=" ")
        print()


gridprint(solver(grid))
