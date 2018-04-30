def color_pixel(grid, x, y, c):
    grid[x - 1][y - 1] = c
    return grid


def vline(grid, x, y1, y2, c):
    for i in range(y2 - y1 + 1):
        grid[y1 + i - 1][x - 1] = c
    return grid

def hline(grid, x1, x2, y, c):
    for i in range(x2 - x1 + 1):
        grid[y - 1][x1 + i - 1] = c
    return grid

def rectangle(grid, x1, y1, x2, y2, c):
    for y in range(y2 - y1 + 1):
        for x in range(x2 - x1 + 1):
            grid[y1 + y - 1][x1 + x - 1] = c
    return grid

def fill(grid, x, y, c, current):
    grid[y][x] = c
    try:
        if grid[y][x + 1] == current:
            fill(grid, x + 1, y, c, current)
    except IndexError:
        pass
    try:
        if grid[y][x - 1] == current:
            fill(grid, x - 1, y, c, current)
    except IndexError:
        pass
    try:
        if grid[y + 1][x] == current:
            fill(grid, x, y + 1, c, current)
    except IndexError:
        pass
    try:
        if grid[y - 1][x] == current:
            fill(grid, x, y - 1, c, current)
    except IndexError:
        pass
    return grid

def main():
    while True:
        command = input().split()
        edit = command[0]

        if edit == "X":
            break
        elif edit == "I":
            image = [["O" for g in range(int(command[1]))] for h in range(int(command[2]))]
        elif edit == "L":
            image = color_pixel(image, int(command[2]), int(command[1]), command[3])
        elif edit == "S":
            print(command[1])
            for i in image:
                print("".join(i))
        elif edit == "V":
            image = vline(image, int(command[1]), int(command[2]), int(command[3]), command[4])
        elif edit == "H":
            image = hline(image, int(command[1]), int(command[2]), int(command[3]), command[4])
        elif edit == "K":
            image = rectangle(image, int(command[1]), int(command[2]), int(command[3]), int(command[4]), command[5])
        elif edit == "F":
            image = fill(image, (int(command[1]) - 1), (int(command[2]) - 1), command[3], image[int(command[2])][int(command[1])])
        elif edit == "C":
            image = [["O" for g in range(len(image[0]))] for h in range(len(image))]


if __name__ == "__main__":
    main()
