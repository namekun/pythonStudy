# 가짜 동전 찾기 순차탐색 응용버전

def weigh(a, b, c, d):
    fake = 29
    if a <= fake and b >= fake:
        return -1
    elif c <= fake and d >= fake:
        return 1
    else:
        return 0


def findFake(left, right):
    for i in range(left + 1, right + 1):
        # 가장 왼쪽 동전과 나머지 동전을 차례대로 비교
        result = weigh(left, left, i, i)
        if result == -1:  # left 동전이 가벼움
            return left
        elif result == 1:  # 나머지 동전이 가벼움
            return i
        # 두 동전의 무게가 같다면 다음 동전으로

    # 모든 동전의 무게가 같다면, 가짜 동전이 없는 예외 상황
    return -1


n = 100
print(findFake(0, n - 1))
