def solution(number, k):
    answer = ''
    # 아이디어 - stack에 넣어주고, stack에 들어있는 수가 작으면 빼버린다
    stack = [number[0]]

    for i in number[1:]:
        while stack and k>0 and stack[-1]<i:
            stack.pop()         # 빼버림
            k -= 1
        stack.append(i)

    # if k>0:
    #     stack = stack[:-k]

    answer = ''.join(stack)
    return answer

print(solution(number="4321", k=2))

# 221 인데 3이라면