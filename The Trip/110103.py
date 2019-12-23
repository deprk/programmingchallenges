def trip(students):
    cost = 0
    spending = []

    for i in range(students):
        spending.append(float(input()) * 100)
        cost += spending[i]
    avg = cost // students
    leftover = cost - (avg * students)

    cost = 0

    for j in range(students):
        if spending[j] > avg:
            if leftover > 0:
                cost += spending[j] - avg - 1
                leftover -= 1
            else:
                cost += spending[j] - avg
    #print("$" + str(round(cost/100, 2)))
    print("$%.2f" % (cost/ 100.0))

def main():
    while True:
        start = int(input())
        if start != 0:
            trip(start)
        else:
            break


if __name__ == "__main__":
    main()




