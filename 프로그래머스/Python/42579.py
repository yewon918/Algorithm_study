def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            # 현재 장르가 이미 dic에 있다면,
            # 그 장르에 해당하는 value의 0번째 index에 현재 index를 append해주고
            # 1번째 index에 재생횟수를 추가해준다.
            dic[genres[i]][0].append(i)
            dic[genres[i]][1] += plays[i]
        else:
            # 현재 장르가 dic에 없다면 dic에 현재 index와 재생횟수를 추가해준다.
            dic[genres[i]] = [[i], plays[i]]

    print(dic)
    # dic.items()를 재생횟수순으로 내림차순 정렬(-x[1][1])해서 diclist에 할당한다.
    diclist = sorted(dic.items(), key=lambda x: -x[1][1])
    print(diclist)

    for i in diclist:
        print(dic[i[0]])
        # 현재 장르에 속한 곡이 하나라면 하나만 answer에 추가시켜준다.
        if len(dic[i[0]][0]) == 1:
            answer.append(dic[i[0]][0][0])
        else:
            # 현재 장르에 속한 곡이 2개 이상이라면,
            # 재생횟수순으로 내림차순 정렬한 뒤 상위 2개의 곡만 answer에 extend해준다.
            dic[i[0]][0].sort(key=lambda x: -plays[x])
            answer.extend(dic[i[0]][0][:2])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))