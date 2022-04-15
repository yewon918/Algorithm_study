'''
6:17
'''
import heapq
def solution(food_times, k):
    answer = 0
    q = []

    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1)) # 음식이랑 순서 같이

    prev = 0
    now = 0
    total = 0
    flen = len(food_times)

    while total+(q[0][0]-prev)*flen <= k:
        now = heapq.heappop(q)[0]
        total += (now-prev)*flen
        prev = now
        flen -= 1
    result = sorted(q, key = lambda x:x[1])
    answer = result[(k-total)%flen][1]

    return answer

print(solution([4,2,3,6,7,1,5,8], 16))