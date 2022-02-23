def solution(n):
    arr = '124'
    if n <= 3:
        return arr[n - 1]
    n -= 1

    result = []
    def dfs(n):
        if n < 3:
            result.append(arr[n])
            return

        result.append(arr[n % 3])
        dfs(n // 3 - 1)

    dfs(n)

    return ''.join(reversed(result))

print(solution(4))