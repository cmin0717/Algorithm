from heapq import *

def solution(alp, cop, problems):

    # 각 코딩력과 알고력의 최대값을 찾는다.
    max_a,max_c = 0,0
    for p in problems: 
        max_a = max(max_a,p[0])
        max_c = max(max_c,p[1])
    
    h,visit = [], {(alp,cop):0} # 방문체크를 cnt와 함께하기위해 dic사용
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]] # 그냥 1씩올리는 문제도 포함
    heappush(h, [0,alp,cop])
    
    while h:
        
        cnt,a,c = heappop(h)
        
        # 만일 최대값에 둘다 도달했다면 현재 cnt 출력
        if a >= max_a and c >= max_c:
            return cnt

        # 문제들을 하나씩 다 돌면서 풀수있다면 풀고 값을 더해준걸 힙에 삽입
        for p in problems:
            if a >= p[0] and c >= p[1]:
                # 두 값은 최대값을 넘지 않는값으로만 지정(사실 잘 이해가 가지않는다. 메모리를 많이 사용해서 그런가?)
                # 시간초과랑은 상관이 없을거같은데...(이걸 몰라서 답을 봤다..)
                x,y = min(a+p[2], max_a), min(c+p[3], max_c)
                if (x,y) not in visit or visit[(x,y)] > cnt +p[4]:
                    heappush(h, [cnt+p[4], x, y])
                    visit[(x,y)] = cnt+p[4]
            
solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])