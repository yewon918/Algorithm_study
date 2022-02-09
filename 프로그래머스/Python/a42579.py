def solution(genres, plays):
    answer = []
    dict = {}

    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]][0].append(i)
            dict[genres[i]][1] += plays[i]
        else:
            dict[genres[i]] = [[i], plays[i]]

    #print(dict)
    dict_list = sorted(dict.items(), key=lambda x: -x[1][1])
    # dict.items를 정렬할건데, lambda를 사용할것.: value의 [1]인덱스 사용
    #print(dict_list)

    for j in dict_list:
        if len(dict[j[0]][0]) == 1:
            answer.append(dict[j[0]][0][0])
        else:
            dict[j[0]][0].sort(key=lambda x: -plays[x])
            answer.extend(dict[j[0]][0][:2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))