'''
괄호 개수는 맞고 짝이 안맞음
괄호를 모두 뽑아 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램
() 개수 같음: 균형잡힌 괄호 문자열
() 짝이 맞음: 올바른 괄호 문자열 - 서로 뒤집혀있으면 안됨
u - 균형잡힌 괄호 문자열: 짝수 개, ( ) 개수 서로 확인해야함,
v - 비어있을 수 있음, 재귀수행적으로 수행 빈문자열 반환,
if 올바른 문자열 || 올바르지 않은 문자열
"() || ))(( | ()"
(())()

재귀 - v에 대해
균형잡힌 문자열인지 아닌지 판단 해야함

check correct(w):
    # 균형잡힌 문자열 () 개수 동일
    u 찾는 코드     stack, 빠져나온거 u에 추가,
                  남아있는 개수 확인, 스택에 들어있는 수가 남은거보다 많을 때 정지
    v 나머지

    # u가 올바른지 아닌지 판단
    올바른 문자열이라면
        v가 빈 문자열이 아니라면 check correct(v)
        return u+v

    올바른 문자열이 아니라면
        빈문자열 ( + correct(v) + )
        u의 첫번째, 마지막 문자 제거, 괄호 방향 뒤집어서 뒤에 붙임
    return 최종 문자열


'''
def correct(w):
    # 균형있는 문자열
    stack = []
    u = []
    v = []
    for i in range(len(w)):
        if len(stack) == 0:
            stack.append(w[i])
        else:
            if stack[-1] == '(' and w[i] == ')':
                u.append(stack.pop())
                u.append(w[i])
                continue
            else:
                stack.append(w[i])
        if len(stack) > len(w[i:]):
            v+=stack
            v+=w[i:]        # append하면 []도 그대로 들어감
            break

    # 올바른 문자열
    empty = []
    new_u = []
    if u[0] == '(' and u[-1] == ')':    # 올바름
        return u+correct(v)
    else:
        empty.append('(' + correct(v) + ')')
        # u 처음, 마지막 제거, 괄호 방향 뒤집어서 뒤에 붙이기
        for j in range(1, len(u)-1):
            if u[j] == '(':
                new_u += ')'
            else:
                new_u += '('
        return empty + new_u


def solution(p):
    answer = ''
    p = list(p)
    answer = correct(p)
    return answer

print(solution("()))((()"))