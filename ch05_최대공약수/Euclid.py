# 유클리드는 최대공약수에 다음과 같은 규칙이 있는 것을 발견했다
# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다. 즉 gcd(a, b) = gcd(b, a%b)인것
# 어떤 수와 0의 최대 공약수는 자기 자신이다. 즉 gcd(n, 0) = n이다.
# 이 방식을 이용해서 재귀형식의 최대공약수 구하는 알고리즘을 만들어보자

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(81, 39))



















