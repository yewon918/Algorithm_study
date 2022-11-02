'''
마디 의 길이 출력
최대 길이 10
반복되는 문자가 총 몇개인지 출력

len(sent)-1 만큼만 반복될 경우 한 마디
'''

num = int(input())
for i in range(num):
    sent = input()
    save = sent

    for s in range(1, len(sent)):    # 자르는 길이
        if len(sent) == 0:
            break
        sent = save         # 리셋
        front = sent[:s]
        sent = sent[s:]

        while len(sent)//s+1:
            now = sent[:s]
            sent = sent[s:]
            if now == front:    # 비어있지 않고 동일하다면 끝까지 확인함
                front = now
                answer = len(front)
            else: break
    print("#{} {}".format(i+1, answer))
