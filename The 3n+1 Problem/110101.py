def collatz(i, j):

    difference = j - i
    count = 0
    greatest = 0

    while count <= difference:
        seq = sequence(i + count)
        if seq > greatest:
            greatest = seq
        count += 1

    print(str(i) + " " + str(j) + " " + str(greatest + 1) + " ")

def sequence(n):
    sequencecount = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        sequencecount += 1
    return sequencecount

def main():
    while True:
        try:
            series = input().split()
            start = int(series[0])
            end = int(series[1])
            collatz(start, end)
        except EOFError:
            break

if __name__ == "__main__":
    main()





