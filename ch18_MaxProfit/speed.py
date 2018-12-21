# 최대 수익 문제를 푸는 두 알고리즘의 계산 속도 비교하기
# 걸린 시간을 출력/ 비교한다.

import time
import random

# 느린 알고리즘

def slowMaxProfit(prices):
    n = len(prices)
    maxPro = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]

            if profit > maxPro:
                maxPro = profit

    return maxPro

# 빠른 알고리즘
def speedMaxProfit(prices):
    n = len(prices)
    maxPro = 0
    minPrice = prices[0]

    for x in range(1, n):
        profit = prices[x] - minPrice
        if profit > maxPro:
            maxPro = profit

        if prices[x] < minPrice:
            minPrice = prices[x]

    return maxPro

def test(n):
    # 난수로 테스트 자료 만들기

    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))

    # 느린 알고리즘 테스트
    start = time.time()
    mps = slowMaxProfit(a)
    end = time.time()
    time_slow = end - start

    # 빠른 알고리즘 테스트
    start = time.time()
    mpf = speedMaxProfit(a)
    end = time.time()
    time_fast = end - start

    # 결과 출력
    print(n, mps, mpf)

    # 결과 출력 : 계산 결과 비교
    m = 0 # 느린 알고리즘과 빠른 알고리즘의 수행 시간 비율을 저장할 변수
    if time_fast > 0: # 컴퓨터 환경에 따라 빠른 알고리즘 시간이 0으로 측정될 수 있음
        # 이럴때는 0을 출력
        m = time_slow / time_fast
    # 입력크기, 느린 알고리즘 수행시간, 빠른 알고리즘 수행시간, 계산 시간 차이
    # %d는 정수 출력,  %.5f 는 소수점 다섯 자리까지의 출력을 의미
    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))


test(100)
test(10000)

