'''
answers - 1번부터 마지막 문제까지 정답이 순서대로
return: 가장 많은 문제 맞힌 사람 / 배열
------
while문 안에서 answers가 없어질때까지
반복문을 돌려서 확인
1,2,3의 각각의 배열이 있고, answer과 길이가 같아질때까지 반복문으로 임시를 만듦
strcmp를 통해 얼마나 같은지 찾고 배열로 반환

'''

def solution(answers):
    answer = [] # set으로
    s1 = [1,2,3,4,5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    tmp1=[]
    tmp2=[]
    tmp3=[]
    one, two, three = 0,0,0

    for i in range(0, len(answers)+1):  # 반복적으로 tmp 배열들 만들기
        tmp1.append(s1[i%len(s1)])
        tmp2.append(s2[i%len(s2)])
        tmp3.append(s3[i%len(s3)])

    for j in range(len(answers)):
        if tmp1[j] == answers[j]:
            one+=1
        if tmp2[j] == answers[j]:
            two+=1
        if tmp3[j] == answers[j]:
            three+=1

    m = max(one, two, three)
    if m == one:
        answer.append(1)
    if m == two:
        answer.append(2)
    if m == three:
        answer.append(3)

    return answer

print(solution(answers=[1,3,2,4,2]))