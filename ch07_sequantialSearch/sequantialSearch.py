# list에서 특정 숫자의 위치 찾기
# input : 리스트 a , 찾는 값 x

def search(a, x):
    n = len(a)

    for i in range(0, n):
        if a[i] == x:
            return i

    return -1


a = [1, 3, 6, 8, 5]

print(search(a, 5))
