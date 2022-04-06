from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    candidate = set()

    if len(user_id)==len(banned_id):
        return 1

    for candi in permutations(user_id, len(banned_id)):
        count = 0
        for idx in range(len(banned_id)):
            if len(candi[idx]) == len(banned_id[idx]):
                if check(candi[idx], banned_id[idx]) == False:
                    break
                else:
                    count += 1
                if count == len(banned_id):
                    candidate = set(candi)
                    if candidate not in answer:
                        answer.append(candidate)


    return len(answer)

def check(ncheck, banned):
    for j in range(len(banned)):
        if banned[j] == '*':
            continue
        if banned[j] == ncheck[j]:
            continue
        else:
            return False
    return True

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))