'''
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장짧은 구간
시작 진열대 번호 가장 작은 구간 return
인덱스 1부터 시작
----
set - 진열된 보석 종류 파악 필요
차례대로 검사하기
범위를 조금씩 늘리기 -> n칸, n+1칸씩 확인
범위 안에 보석 종류가 전부 있는지, 없다면 범위 한칸씩 뒤로 밀려나기
없다면 범위 +1 하고 한칸씩 뒤로 밀어내기

'''
def solution(gems):
    answer = [1, len(gems)]
    gem_list = set(gems)
    gem_size = len(gem_list)

    size = 0
    while size < len(gems)-gem_size:
        for i in range(0, len(gems)-gem_size+1):
            if set(gems[i:gem_size+i+size]) == gem_list:
                answer = [i+1, gem_size+i+size]
                return answer

        size += 1


    return answer

print(solution(	["AA", "AB", "AC", "AA", "AC"]))