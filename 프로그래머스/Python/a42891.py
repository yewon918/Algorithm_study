import heapq
def solution(food_times, k):
    answer = 0

    if sum(food_times)<=k:
        return -1
    q = []

    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    total_time=0  #전체 걸린 시간
    prev=0
    length=len(food_times)

    while total_time+(q[0][0]-prev)*length<=k:   #음식 다먹는데 걸리는 시간이 k이하일때
        now = heapq.heappop(q)[0]
        total_time += (now-prev)*length
        length -= 1
        prev = now
    res=sorted(q,key=lambda x:x[1])  #번호순으로 정렬

    return res[(k-total_time)%length][1]