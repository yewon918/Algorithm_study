def solution(N, number):
    answer = -1     # 8보다 크면 -1을 반환한다
    dp = []
    dp.append([0])
    dp.append([N])

    if number == N:
        answer = 1
    else:
        for seq in range(2, 9):
            num = {int(str(N)*seq)}   # 그냥 붙어있는 경우 고려
            for i in range(1, seq):
                for j in dp[i]:
                    for k in dp[seq-i]:
                        num.add(j+k)
                        num.add(j-k)
                        num.add(j*k)
                        if k!= 0:
                            num.add(j//k)
            arr_num = list(num)
            if number in arr_num:
                answer = seq
            else:
                dp.append(arr_num)

    return answer

print(solution(2, 11))