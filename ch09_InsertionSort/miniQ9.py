# 내림차순의 삽입정렬 구현하기

def insSortDesc(x):
    for i in range(1, len(x)):
        val = x[i]
        j = i - 1
        # desc의 경우에는 작은수가 큰수의 뒤로 가야하기 때문에 아래와 같이 바꿔줘야한다.
        while j >= 0 and x[j] < val:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = val

    return x

d = [2, 1, 5, 3, 4]

print(insSortDesc(d))