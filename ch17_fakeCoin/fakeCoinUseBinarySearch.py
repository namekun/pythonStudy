# 가짜 동전 찾기 알고리즘


def weigh(a, b, c, d):
    fake = 29
    if a <= fake and b >= fake:
        return -1
    elif c <= fake and d >= fake:
        return 1
    else:
        return 0


def findFake(left, right):
    # 만약 오른쪽과 왼쪽의 위치가 같아진다면, 가짜동전의 위치를 찾은 것이니 return 해준다.
    if left == right:
        return left

    half = (right - left + 1) // 2  # 0부터 n-1번째까지라서 + 1 해줘야한다.

    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weigh(g1_left, g1_right, g2_left, g2_right)

    if result == 1:
        return findFake(g2_left, g2_right)
    elif result == -1:
        return findFake(g1_left, g1_right)
    else:  # 두 집단의 무게가 같다면?
        return right  # 두 그룹으로 나뉘지않고, 마지막 한 개 남은 동전이 가짜동전이다.


n = 100
print(findFake(0, n - 1))
