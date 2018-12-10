# 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보자

def findMaxRec(a, n):
    if n == 1:
        return a[0]
    maxV = findMaxRec(a, n - 1)
    if maxV > a[n - 1]:
        return maxV
    else:
        return a[n - 1]


v = [34, 32, 12, 6, 7, 68, 70, 768, 54]

print(findMaxRec(v, len(v)))