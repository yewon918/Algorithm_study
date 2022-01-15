'''

'''
def solution(s):
    answer = len(s)
    cnt = 1
    comp =[]
    for i in range(1, len(s)//2+1):
        first = s[0:i]
        for j in range(i, len(s)+1, i):
            if first == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    comp += str(cnt)+first
                else: comp += first
                cnt = 1
            first = s[j:j+i]
        comp += s[j:]

        answer = min(answer, len(comp))
        comp.clear()

    return answer

print(solution(s="aabbaccc"))