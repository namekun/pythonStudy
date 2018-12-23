def solution(clothes):
    answer = 1
    hash_map = dict()
    n = len(clothes)

    for i in range(n):
        if clothes[i][1] in hash_map:
            hash_map[clothes[i][1]] += 1
        else:
            hash_map[clothes[i][1]] = 1

    for j in hash_map:
        answer *= (hash_map[j] + 1)

    answer -= 1

    return answer


c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["jeans", "pants"]]

print(solution(c))

