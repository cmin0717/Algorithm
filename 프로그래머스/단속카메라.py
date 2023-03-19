def solution(routes):
    routes.sort(key=lambda x:(x[1],x[0])) # 도착지,출발지 순으로 정렬 / 도착시간이 빠른 순으로 카메라 설치
    check = set()
    total = 0

    for i in range(len(routes)):
        if i in check: continue # 전에 설치한 카메라에 이미 잡힌경우
        s,e = routes[i]
        total += 1
        for j in range(i+1, len(routes)):
            # 현재 차의 출발 ~ 도착 사이에 출발하는 차, 현재 차의 위치를 포함하는 차
            if s <= routes[j][0] <= e or (s >= routes[j][0] and  e <= routes[j][1]):
                check.add(j) # 같이 카메라에 담는다.
            else:
                break
    return total
solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3],[18,20]])