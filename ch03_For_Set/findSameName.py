# 두번 이상 나온 이름 찾기
# 입력 : 이름이 n개 들어있는 리스트
# 출력 : 이름 n개 중 반복되는 이름의 집합

def findSameName(a):
    n = len(a)

    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


name = ['Tom', 'Jerry', 'Mike', 'Tom']

print(findSameName(name))
