def solution(n, results):
    link = [[float('inf')]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        link[i][i] = 0
    for info in results:
        # 승패 결과를 통해 각 정보를 각 선수에 입력
        link[info[1]][info[0]] = -1 # 패
        link[info[0]][info[1]] = 1 # 승
    
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if link[a][k] == link[k][b] == 1: # a가 k을 기기고 k 가 b를 이겼다면
                    link[a][b] = 1 # a가 b를 이긴경우랑 같다.
                    link[b][a],link[b][k],link[k][a] = -1,-1,-1 # 그렇기에 여기에서는 진거와 같다.
    
    result = 0
    for i in range(1,n+1):
        if float('inf') not in link[i][1:]: # 각 선수의 정보에 초기값 inf가 없다면 순위를 확실히 정할수 있는 경우이다.
            result += 1
    return result

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

# 플로이드 워샬 알고리즘 : 한 정점에서 각 모든 노드까지의 최단거리 구하는 알고리즘
# 현재 문제에서는 주어진 정보를 가지고 a = b, b = c일경우 a=c라는 점화식을 통해 승패를 추측