def display(size, num):
    n = len(num)
    grid = [[0 for g in range(n)] for h in range(2 * size + 3)]

    for i in range(n):
        m = num[i]
        if i == (n - 1):
            if m != 4 and m != 1:
                grid[0][i] = " " + "-" * size + " "
            else:
                grid[0][i] = " " * (size + 2)
            if m in [1, 2, 3, 7]:
                for j in range(size):
                    grid[1 + j][i] = " " * (size + 1) + "|"
            elif m in [4, 8, 9, 0]:
                for j in range(size):
                    grid[1 + j][i] = "|" + " " * size + "|"
            else:
                for j in range(size):
                    grid[1 + j][i] = "|" + " " * (size + 1)
            if m in [1, 7, 0]:
                grid[size + 1][i] = " " * (size + 2)
            else:
                grid[size + 1][i] = " " + "-" * size + " "
            if m == 2:
                for j in range(size):
                    grid[size + 2 + j][i] = "|" + " " * (size + 1)
            elif m in [6, 8, 0]:
                for j in range(size):
                    grid[size + 2 + j][i] = "|" + " " * size + "|"
            else:
                for j in range(size):
                    grid[size + 2 + j][i] = " " * (size + 1) + "|"
            if m in [1, 4, 7]:
                grid[2 * size + 2][i] = " " * (size + 2)
            else:
                grid[2 * size + 2][i] = " " + "-" * size + " "

        else:
            if m != 4 and m != 1:
                grid[0][i] = " " + "-" * size + "  "
            else:
                grid[0][i] = " " * (size + 3)

            if m in [1, 2, 3, 7]:
                for j in range(size):
                    grid[1 + j][i] = " " * (size + 1) + "| "
            elif m in [4, 8, 9, 0]:
                for j in range(size):
                    grid[1 + j][i] = "|" + " " * size + "| "
            else:
                for j in range(size):
                    grid[1 + j][i] = "|" + " " * (size + 1) + " "

            if m in [1, 7, 0]:
                grid[size + 1][i] = " " * (size + 3)
            else:
                grid[size + 1][i] = " " + "-" * size + "  "

            if m == 2:
                for j in range(size):
                    grid[size + 2 + j][i] = "|" + " " * (size + 1) + " "
            elif m in [6, 8, 0]:
                for j in range(size):
                    grid[size + 2 + j][i] = "|" + " " * size + "| "
            else:
                for j in range(size):
                    grid[size + 2 + j][i] = " " * (size + 1) + "| "

            if m in [1, 4, 7]:
                grid[2 * size + 2][i] = " " * (size + 3)
            else:
                grid[2 * size + 2][i] = " " + "-" * size + "  "

    for q in grid:
        print("".join(q))
    print()

def main():
    while True:
        inp = input().split()
        size = int(inp[0])
        num = [int(x) for x in inp[1]]

        if size == 0:
            break
        else:
            display(size, num)


if __name__ == "__main__":
    main()
