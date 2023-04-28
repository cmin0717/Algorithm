from heapq import *

def solution(n, paths, gates, summits):
    
    link = [[] for _ in range(n+1)]
    
    # 간선 정보를 link에 담는다.
    for x,y,c in paths:
        link[x].append([c,y])
        link[y].append([c,x])
    
    gates,summits = set(gates),set(summits) # 중복되는 지점은 삭제
    h, dist = [], [float('inf') for _ in range(n+1)]
    
    # 각 출발점을 힙에 넣어준다.
    for g in gates:
        dist[g] = 0
        heappush(h, [dist[g],g])

    # 다익스트라를 변형하여 최단거리가 아닌 간선의 최단거리로 배열을 구한다.
    while h:
        cnt,idx = heappop(h)

        if dist[idx] < cnt: continue

        for c,i in link[idx]:
            new_dist = max(c, cnt)
            if dist[i] > new_dist:
                dist[i] = new_dist
                if i not in summits:
                    heappush(h, [dist[i],i])

    # 구해진 배열을 사용하여 최대 간선의 값이 최단간선인 가진 경로를 찾는다.
    result = []
    for s in summits:
        result.append([s,dist[s]])
    result.sort(key=lambda x: (x[1],x[0]))
    return result[0]

solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])