# DFS - 깊이 우선 탐색
# 탐색 순서 : [1, 2, 4, 5, 3]

graphInfo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}


def dfs(g, start):
    stack = []
    visited = list()

    stack.append(start)

    while stack:
        n = stack.pop()  # 스택에서 하나 꺼낸다.
        visited.append(n)
        for x in g[n]:
            if x not in visited:
                stack.append(x)
    return visited


print(dfs(graphInfo, 1))
