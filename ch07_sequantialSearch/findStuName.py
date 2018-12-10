def findS(a, b, x):
    n = len(a)

    for i in range(0, n):
        if x == a[i]:
            return b[i]


stu_no = [39, 14, 67, 105]
stu_name = ['justin', 'john', 'mike', 'Summer']

print(findS(stu_no, stu_name, 14))