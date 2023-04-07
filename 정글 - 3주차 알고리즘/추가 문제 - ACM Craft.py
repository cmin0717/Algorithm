from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n,k = map(int,input().split())
    time = [0] + list(map(int,input().split())) # 인덱스를 편하게 쓰기 위해 앞에 [0] 추가, dp를 만들어서 하려고했는데 굳이 안써도 되서 이걸로 다 사용
    li = [[] for _ in range(n+1)]  # 각 인덱스에 해당하는 건물을 지으면 다음 건물을 생성할수있는 애들을 모아두는곳
    li2 = [[] for _ in range(n+1)] # 각 인덱스에 해당하는 건물을 짓기 위해 필요한 애들을 넣어두는곳
    degree = [0] * (n+1) # 진입 차수

    for _ in range(k):
        x,y = map(int,input().split())
        li[x].append(y)
        li2[y].append(x)
        degree[y] += 1

    end = int(input())

    dq = deque()
    for i in range(1,n+1): # 진입 차수가 0인 애들을 미리 dq에 넣어두었다.
        if degree[i] == 0 and i != end:
            dq.append(i)
            
    while dq:
        idx = dq.popleft()
        if len(li2[idx]) != 0: # 이 조건은 결국 진입차수가 있는 애들만 참인 조건이다.
            check = []
            for i in li2[idx]:
                check.append(time[i])
            time[idx] = max(check) + time[idx] # 어차피 최대값을 구하는 거니깐 요런식으로
        for i in li[idx]:
            degree[i] -= 1
            if degree[i] == 0: # 진입 차수가 0이되면 넣어준다.
                dq.append(i)
    print(time[end])


# dfs로 접근했는데 58퍼쯤에서 떙! dp랑 위상정렬 쪽으로 좋은 생각이 나서 마무리 안하고 끝냄
# def dfs(x,t):
#     if check[x] == 0:
#         t += time[x-1]
#         check[x] = 1
#         for i in li[x]:
#             if check[i] == 0:
#                 t = dfs(i,t)
#     return t

# for _ in range(test_case):

#     n,k = map(int,input().split())
#     time = list(map(int,input().split()))
#     li = [[] for _ in range(n+1)]
#     for o in range(k):
#         x,y = map(int,input().split())
#         li[y].append(x)

#     start = int(input())
#     result_time = [time[start-1]]

#     for i in li[start]:
#         check = [0] * (n+1)
#         x = dfs(i,time[start-1])
#         result_time.append(x)

#     print(max(result_time))