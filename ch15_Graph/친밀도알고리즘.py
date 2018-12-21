# 친구리스트에서 자신의 모든 친구를 찾고 친구들의 친밀도를 계산하는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 name
# 출력 : 모든 친구의 이름과 자신과의 친밀도

def findFre(g, name):
    usedName = []
    already = set()

    usedName.append((name, 0))  # 친밀도와 이름을 함께 묶어서 튜플로 처리
    already.add(name)

    while usedName:
        (fre, d) = usedName.pop(0)
        print(fre, d)
        for x in g[fre]:
            if x not in already:
                usedName.append((x, d + 1))
                already.add(x)


freInfo = {
    'summer': ['john', 'justin', 'mike'],
    'john': ['summer', 'justin'],
    'justin': ['john', 'summer', 'mike', 'may'],
    'mike': ['summer', 'justin'],
    'may': ['justin', 'kim'],
    'kim': ['may'],
    'tom': ['jerry'],
    'jerry': ['tom']
}

findFre(freInfo, 'summer')
