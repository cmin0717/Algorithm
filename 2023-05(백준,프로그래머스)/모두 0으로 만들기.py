from collections import deque

def solution(a, edges):
    # 노드의 합이 0이 아니라면 무슨짓을 해도 0이 나올수 없기에 바로 -1 리턴
    if sum(a) != 0: 
        return -1
    
    # 간선정보를 이용하여 트리를 구성하고 각 노드의 진입차수를 넣어준다.
    tree = [[] for _ in range(len(a))]
    degree = [0] * len(a)
    for x,y in edges:
        tree[x].append(y)
        tree[y].append(x)
        degree[x] += 1
        degree[y] += 1
    
    # 현재 트리의 리프 노드를 구한다.
    leaf_nood = [i for i in range(len(tree)) if degree[i] == 1]
    
    # BFS를 이용하여 진입차수가 1인 애들만 q에 넣어 진행한다.
    result, q = 0, deque(leaf_nood)
    while q:
        idx = q.popleft()
        degree[idx] -= 1
        
        for i in tree[idx]:
            if degree[i] > 0:
                # 자신의 노드값을 부모에게 다 넘겨준다.
                result += abs(a[idx])
                a[i] += a[idx]
                a[idx] = 0
                degree[i] -= 1
                # 만일 진입차수가 1이됬다면 q에 넣어준다.
                if degree[i] == 1:
                    q.append(i)
    
    return result