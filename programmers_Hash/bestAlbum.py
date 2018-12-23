from operator import itemgetter


def solution(genres, plays):
    answer = []
    musics = {}

    for i in range(0, len(genres)):
        if genres[i] not in musics:
            musics[genres[i]] = []
            musics[genres[i]].append(0)
        musics[genres[i]].append((i, plays[i]))
        # 플레이 횟수를 더해줘서 가장 앞에 오게 한다.
        musics[genres[i]][0] += plays[i]

    # sort desc

    temp = list(musics.values())
    # 기준은 해당 값의 처음값으로 하고, 내림차순으로 정렬한다.
    # itemgetter는 sort 하고자 하는 list의 item의 1번째 인덱스 기준으로 sort 하는 방식
    temp.sort(key=itemgetter(0), reverse=True)

    # 가장 많이 플레이된 장르를 Pop한다.
    # 그리고 가장 많이 플레이된 두개의 노래를 고른다.
    while temp:
        max = -1

        temp[0].pop(0)

        # 플레이 횟수를 많이된 순으로 정렬
        temp[0].sort(key=itemgetter(1), reverse=True)

        # 가장 플레이 많이 된 두개의 노래를 answer에 append해준다.
        for i in range(0, len(temp[0])):
            if i >= 2:
                break
            answer.append(temp[0][i][0])

        # 현재 장르를 제거한다.
        temp.pop(0)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
