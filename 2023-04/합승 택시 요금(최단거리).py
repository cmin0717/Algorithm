def solution(n, start, a, b, fares):
    graph = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for s,e,c in fares:
        graph[s-1][e-1] = c
        graph[e-1][s-1] = c
    
    # 플로이드 워셜 알고리즘 사용 (다익스트라로 하면 빠른건 되게 빠르게 나오는데 오래걸리는건 더 오래걸린다.)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                
    result = float('inf')
    
    for i in range(n):
        cost = graph[start-1][i] + graph[i][a-1] + graph[i][b-1] # 워셜로 구한 거리마다 비용으로 완.탐 돌려서 최소값 구함
        result = min(result,cost)
    return result

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
