'''
모든 차량이 한번은 카메라를 만나야함, 최소 몇 대가 필요한가
routes = [고속도로 진입지점, 나간지점]

진입 구간으로 sort (오름차순)
첫번째 원소의 진입~나간 에서 하나씩 올려가면서 그 다음의 각 범위에 속하는지 확인
속하는 거 개수 세기

'''
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])      # 진출지점 기준으로 정렬
    cam = -30001

    for route in routes:
        if cam<route[0]:        # 진입지점 보다 작다면 카메라를 갱신시킨다
            answer += 1
            cam = route[1]
    # 갱신시킨 카메라 값이 다음 진출지점보다 클 일은 없어서 범위가 무시 되는게 없음

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))