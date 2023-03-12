from collections import deque
sys.setrecursionlimit(10**6)
import sys
input = sys.stdin.readline

test_case = int(input())

def dfs(x,y):
    global success
    if success == 1: # 연결된 노드끼리 색이겹친다면 이분 그래프가 될수없기에 return
        return
    check[x] = y # 색을 정해준다.
    for i in li[x]:
        if check[i] == 0:
            dfs(i,-y) # 연결된쪽으로 넘어갈때는 색을 바꾸어준다.
        else:
            if check[x] == check[i]: # 연결된거 끼리 색이 같다면
                success = 1 # 이분 그래프가 아니라는 표시를 해준다.
                return

for _ in range(test_case):

    v,e = map(int,input().split())
    li = [[] for _ in range(v+1)]
    check = [0] * (v+1)
    success = 0

    for _ in range(e):
        x,y = map(int,input().split())
        li[x].append(y)
        li[y].append(x)

    for i in range(1,v+1): # 모든 노드가 연결되어 있는것이 아니기 떄문에 각 출발지에서 다 해봐야한다.
        if check[i] == 0:
            dfs(i,1)
            if success == 1:
                print('NO')
                break
    else:
        print('YES')
    

# bfs 실패함 아예 연결되지 않은 경우를 해결하지못함 해결을 해도 시간초과나옴
# def bfs(x):
#     global check

#     dq = deque([[x,1]])
#     node[x] = 1

#     while dq:
#         if check == 1:
#             return False

#         element = dq.popleft()
#         if element[1] == 1:
#             new_check = 0
#         else:
#             new_check = 1

#         for i in li[element[0]]:
#             if node[i] == 0:
#                 node[i] = new_check
#                 dq.append([i,new_check])
#             else:
#                 if node[i] == element[1]:
#                     check = 1
#                     break
#     else:
#         return True