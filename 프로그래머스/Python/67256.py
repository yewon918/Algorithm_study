def solution(numbers, hand):
    answer = ''
    left = (3, 0)
    right = (3, 2)
    keypad = [(3,1),
           (0,0), (0,1), (0,2),
           (1,0), (1,1), (1,2),
           (2,0), (2,1), (2,2)
           ]


    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = keypad[num]
        elif num in [3,6,9]:
            answer += 'R'
            right = keypad[num]
        else:       # 좌표느낌?
            lmove = abs(keypad[num][0]-left[0]) + abs(keypad[num][1]-left[1])
            rmove = abs(keypad[num][0]-right[0]) + abs(keypad[num][1]-right[1])
            if lmove > rmove:
                answer += 'R'
                right = keypad[num]
            elif lmove < rmove:
                answer += 'L'
                left = keypad[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = keypad[num]
                else:
                    answer += 'L'
                    left = keypad[num]

    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))