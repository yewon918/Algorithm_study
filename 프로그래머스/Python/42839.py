numbers = "17"

lnum = list(numbers)  # 하나씩 리스트 생성
num = list(map(int, lnum))
answer = 0

for i in num:
    flag = 0
    for y in range(i+1):
        yak = i/y
        if yak != i or yak == y:
            flag = 1
            break
        if flag == 1: break     # 해당 수에 대해 약수구하기 종료, 다음으로
        answer += 1

    for j in num:   # i 뒤에 붙여야하는데 어떻게 하지
        tmp = str(i)+str(j)     # tmp-> list
        um = int(tmp)           # int로 변환
        for y in range(um):
            yak = y/um
            if yak != i or yak == y:
                flag = 1
                break
            if flag == 1: break     # 해당 수에 대해 약수구하기 종료, 다음으로
            answer += 1

        for k in num:
            tmp = str(i) + str(j) + str(k)  # tmp-> list
            um = int(tmp)  # int로 변환
            for y in range(um):
                yak = y / um
                if yak != i or yak == y:
                    flag = 1
                    break
                if flag == 1: break  # 해당 수에 대해 약수구하기 종료, 다음으로
                answer += 1

print(answer)