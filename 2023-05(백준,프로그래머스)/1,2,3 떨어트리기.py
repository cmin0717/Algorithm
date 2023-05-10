from collections import deque

def solution(edges, target):
    n = len(target)
    link = [[] for _ in range(n+1)]
    leaf = [i for i in range(n) if target[i]] # 각 리프노드들을 모아둠

    # 주어진 정보로 트리 형성
    for s,e in edges:
        link[s].append(e)
    for i in range(1,n+1):
        link[i] = deque(sorted(link[i]))

    # 루트노드에서 주어진 규칙으로 도착할 리프노드 리턴
    def find(idx):
        if not link[idx]:
            return idx-1
        link[idx].rotate(-1)
        return find(link[idx][-1])

    # 각 리프노드 값을 달성하기위해 최소,최대 몇번 방문해야하는지 구함
    check = [[] for _ in range(n)]
    for i in range(n):
        if target[i]:
            c = target[i] // 3 if target[i] % 3 == 0 else (target[i] // 3) + 1
            check[i] = [c,target[i]]

    # 위에서 구한 정보를 가지고 각 리프 노드들이 몇번 방문해야하는지 구함
    visit,stay = [0] * n, []
    while True:
        idx = find(1) # 현재 루트노드에서 도착할 리프노드 구함
        visit[idx] += 1 # 리프노드 방문 횟수 +1
        cnt = 0
        # 각각의 리프노드들이 위에서 구한 최소,최대 방문횟수안에 있는지 확인
        for l in leaf:
            # 하나의 리프노드라도 최대값을 넘어가면 주어진 값에 도달할수없기에 바로 -1리턴
            if visit[l] > check[l][1]:
                return [-1]
            if check[l][0] <= visit[l] <= check[l][1]:
                cnt += 1
        stay.append(idx) # 방문한 리프노드 순서대로 저장
        # 만일 모든 리프노드가 최소,최대 범위안에있다면 종료
        if cnt == len(leaf):
            break
    
    # 구한 각 노드들의 방문횟수를 통해 1,2,3 값을 적절히 배분후 노드번호를 키값으로 딕셔너리에 담는다.
    dic = {}
    for s in stay:
        element = [3]*visit[s]
        tt,idx = (visit[s] * 3) - target[s], 0
        while tt > 0:
            element[idx] = 1 if tt >= 3 else element[idx]-tt
            tt -= 2
            idx += 1
        dic[s] = deque(element)

    # 위에서 구한 방문한 리프노드 순서대로 딕셔너리에서 값을 하나씩 뺴서 결과값 출력
    return [dic[s].popleft() for s in stay]


# 불필요한 코드가 있어서 디벨롭했다.(구버전)
# from collections import deque

# def solution(edges, target):
#     n = len(target)
#     link = [[] for _ in range(n+1)]

#     # 주어진 배열로 트리 형성
#     for s,e in edges:
#         link[s].append(e)
#     for i in range(1,n+1):
#         link[i] = deque(sorted(link[i]))

#     turn = []
#     # 규칙에 따라 루트노드에서 시작하여 이번에 끝나는 리프노드를 찾는 함수
#     def find(idx):
#         if not link[idx]:
#             turn.append(idx)
#             return
#         find(link[idx][0])
#         link[idx].rotate(-1) # 간선 변경

#     # 결국 계속 하다보면 반복되는 리프노드들의 구간이 있다 그걸 찾아서 리턴
#     while True:
#         find(1)
#         mid = len(turn) // 2
#         if turn[:mid] == turn[mid:]:
#             turn = deque(turn[:mid])
#             break
    
#     # 각 리프노드들의 값을 만들기위해 최소,최대로 방문해야하는 값을 찾는다.
#     new_t = []
#     visit = [0] * n
#     check = [[] for _ in range(n)]
#     for i in range(n):
#         if target[i]:
#             c = target[i] // 3 if target[i] % 3 == 0 else (target[i] // 3) + 1
#             check[i] = [c,target[i]]
#             new_t.append(i)
    
#     # 아까 구한 반복 구간을 계속 돌면서 위에서 찾아논 최소,최대값 사이에 모든 리프노드가 올때까지 돌린다.
#     stay = [] # 해당 과정에서 방문하는 리프노드를 순서대로 저장
#     while True:
#         cnt = 0
#         for t in new_t:
#             # 만일 하나라도 최대 방문횟수를 넘어가면 만들수 없는 값이기에 바로 -1 리턴
#             if visit[t] > check[t][1]:
#                 return [-1]
#             if check[t][0] <= visit[t] <= check[t][1]:
#                 cnt += 1
#         if cnt == len(new_t):
#             break
#         visit[turn[0]-1] += 1
#         stay.append(turn[0])
#         turn.rotate(-1)
    
#     # 위의 과정으로 정확히 몇번을 방문인지를 알았으니 방문횟수에 맞게 알맞은 값으로 나누어 넣어준다.
#     dic = {}
#     for i in range(n):
#         if visit[i]:
#             element = [3]*visit[i] # 일단 모두 최대값인 3으로 방문횟수만큼 생성
#             tt,idx = (visit[i] * 3) - target[i], 0 # 빼야할 값, 시작 인덱스
#             # 빼야할 값이 0이될때까지 앞쪽부터 뺀다
#             while tt > 0:
#                 if tt >= 3:
#                     element[idx] = 1
#                     tt -= 2
#                 else:
#                     element[idx] -= tt
#                     tt = 0
#                 idx += 1
#             # 그렇게 구한 알맞은 값을 각 리프노드 번호를 키값으로 딕셔너리 저장
#             dic[i+1] = deque(element)
    
#     # 위에서 구한 리프노드 방문 순서를 가지고 딕셔너리에서 하나씩 빼서 result에 저장 후 출력
#     result = []
#     for s in stay:
#         result.append(dic[s].popleft())
#     return result
        
# solution([[1, 2], [1, 3]], [0, 7, 3])