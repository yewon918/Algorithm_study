'''
학생들 번호 - 체격순 : 바로 앞, 바로 뒤만 가능
최대한 많은 학생이 수업 듣도록

체육복 도난 학생 번호 lost
여벌 학생 번호 reserve
return 체육수업을 듣는 학생 최댓값
전체학생: 2<=n<=30
도난 1<=  <=n, 중복 없음
reserve에 있어야만 체육복 빌려줄 수 있음
reserve에 있어도 체육복 도난ㅇ - 하나만 도난, 다른 학생에게 빌려줄수 있음

reserve - 체육복 2개, 한개 도난시 빌려줄 수 있음.

lost 원소가 not in reserve
lost 원소 + 1 || lost -1 in reserve

n까지 훑으면서, lost / reserve 확인, 둘 다 없으면 answer +=1
lost에 reserve의 +-1 이 있다면 lost에서 lost.remove(i-1) remove(i+1)
reserve, lost 중복이면 answer -=1

'''
def solution(n, lost, reserve):
    answer = set([])
    sum = 0
    tmp = []
    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                tmp.append(i)   # 일단 넣어두기
        else:
            if i in reserve:
                answer.add(i + 1)
                answer.add(i - 1)
            else:
                answer.add(i)
    for i in tmp:
        if i not in answer:
            answer.add(i)
            continue
        if i-1 not in answer:
            answer.add(i-1)
            continue
        if i+1 not in answer:
            answer.add(i+1)
            continue

    answer.remove(0)
    answer.remove(n+1)


    return len(answer)

print(solution(5, lost=[2,4], reserve=[1,3,5]))



