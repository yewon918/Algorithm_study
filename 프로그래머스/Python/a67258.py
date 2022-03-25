def solution(gems):
    answer = []
    gem_list = set(gems)    # 보석 종류
    gem_size = len(gem_list)

    gem_range = dict()      # 보석을 사야하는 범위
    gem_range[gems[0]] = 1

    left = 0
    right = 1
    while left < right:
        if gem_size == len(gem_range):
            answer.append((right-left, left, right))

            if gem_range[gems[left]] > 0:
                gem_range[gems[left]] -= 1
            if gem_range[gems[left]] == 0:
                del(gem_range[gems[left]])
            left += 1

        elif gem_size > len(gem_range):
            if right < len(gems):
                gem_range[gems[right]] = gem_range.get(gems[right], 0)+1
                right += 1
            else:       # right >= len(gems)
                break
        else:       # gem_size < len(gem_range)
            if gem_range[left] > 0:
                gem_range[left] -= 1
            elif gem_range[left] == 0:
                del(gem_range[left])
            left += 1

    answer.sort()
    return [answer[0][1]+1, answer[0][2]]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))