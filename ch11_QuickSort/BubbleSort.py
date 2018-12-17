def bubbleSort(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


d = [6, 8, 4, 9, 10, 1, 2, 3, 7, 5]

bubbleSort(d)

print(d)
