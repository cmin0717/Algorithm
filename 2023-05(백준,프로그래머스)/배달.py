from collections import deque

def solution(N, road, K):
    # 간선 정보로 트리 형성
    link = [[] for _ in range(N+1)]
    for x,y,c in road:
        link[x].append([c,y])
        link[y].append([c,x])
    
    # 다익스트라 실행
    dist = [float('inf')] * (N+1)
    q = deque([[0,1]])
    
    while q:
        c, idx = q.popleft()
        
        if dist[idx] < c:
            continue
        
        dist[idx] = c
        for info in link[idx]:
            if c+info[0] < dist[info[1]]:
                q.append([c+info[0], info[1]])
    
    return len([i for i in dist[1:] if i <= K])
    