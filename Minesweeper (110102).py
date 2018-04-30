import sys

def create():
    grid = input().split(" ")
    x = int(grid[0])
    y = int(grid[1])
    grid = [[0 for g in range(y)] for h in range(x)]

    for i in x:
        line = list(input())
        for j in line:
            if line[j - 1] == "*":
                grid[i-1][j-1] = "*"
                if 1 < i < x and 1 < j < y:
                    grid[i + 1][j + 1] += 1
                    grid[i + 1]



