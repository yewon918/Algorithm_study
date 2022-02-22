def solution(record):
    answer = []
    save = {}
    inout = {'Enter': '님이 들어왔습니다', 'Leave': '님이 나갔습니다.'}

    for rec in record:
        rec = rec.split(' ')
        if rec[0] == 'Enter' or rec[0] == 'Change':
            save[rec[1]] = rec[2]

    for sec in record:
        sec = sec.split(' ')
        if sec[0] != 'Change':
            answer.append(save[sec[1]]+inout[sec[0]])

    return answer

print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"
                ]))