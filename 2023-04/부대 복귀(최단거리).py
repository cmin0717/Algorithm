from heapq import *

def solution(n, roads, sources, destination):
    dist = [float('inf')]*(n+1)
    link = [[] for _ in range(n+1)]
    for s,e in roads:
        link[s].append([1,e])
        link[e].append([1,s])
    
    h = []
    heappush(h,[0,destination])
    dist[destination] = 0
    
    while h:
        dis, idx = heappop(h)

        if dist[idx] < dis:
            continue

        for info in link[idx]:
            new_dist = info[0] + dist[idx]
            if new_dist < dist[info[1]]:
                dist[info[1]] = new_dist
                heappush(h, [new_dist, info[1]])
    
    result = []
    for i in sources:
        if dist[i] == float('inf'):
            result.append(-1)
        else:
            result.append(dist[i])
    return result

solution(3,[[1, 2], [2, 3]],[2, 3],1)