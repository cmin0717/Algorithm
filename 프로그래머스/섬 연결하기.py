parent = []

# 재귀적으로 자신과 연관된 노드의 통일 값을 가져온다.
def find(p,x):
    if p[x] != x:
        p[x] = find(p,p[x])
    return p[x]

# 두개의 노드의 값을 하나로 통일
def union(p,x,y):
    a = find(p,x)
    b = find(p,y)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def solution(n, costs):
    global parent
    parent = [i for i in range(n)] # 각 노드들의 초기값 세팅
    costs.sort(key=lambda x:x[2]) # 간선 비용 기준으로 정렬
    total = 0
    for x,y,c in costs:
        if find(parent, x) != find(parent,y): # 서로의 노드값이 다르다면 사이클이 존재 x니깐 실행
            union(parent,x,y) # 두 노드의 값을 하나로 통일
            total += c

    return total

print(solution(4,[[0, 1, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]))


# 그리디적으로 풀라고 했는데 실패!! mst방식으로 해결해야함
# def solution(n, costs):
#     link = [[] for i in range(n)]
#     for x,y,c in costs:
#         link[x].append([c,y])
#         link[y].append([c,x])
        
#     cost = 0
#     linked = []
#     check = 0
#     for i in range(n):
#         if len(link[i]) == 1:
#             cost += link[i][0][0]
#             linked.append(link[i])
#             check += 2
            
#     costs.sort(key=lambda x:x[2])

#     for x,y,c in costs:
#         if check == (n-1)*2:
#             break
#         cost += c
#         check += 2
#     return cost