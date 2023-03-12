from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

indegree = [0] * (n+1) # 진입 차수

link = [[] for _ in range(n+1)] # 해당 건물을 생성하면 작업 할 수있는 작업의 연결리스트

time_list = [0] * (n+1) # 각 작업들을 하는데 소요되는 시간

time = [0] * (n+1) # 시간 dp

for i in range(1,n+1):
    info = list(map(int,input().split()))
    
    time_list[i] = info[0]

    if info[1] != 0:
        for j in info[2:]:
            link[j].append(i)
            indegree[i] += 1
    else:
        time[i] = info[0] # 진입 차수가 없는 애들은 dp값에 바로 넣어준다.

dq = deque([i for i in range(1,n+1) if indegree[i] == 0]) # 진입 차수가 0인 애들을 미리 넣어둔다.

while dq:
    idx = dq.popleft()

    for i in link[idx]:
        time[i] = max(time[i], time[idx] + time_list[i]) # 해당 idx에 해당하는 연결리스트에서 가장 큰 값을 dp[i]에 넣는다.
        indegree[i] -= 1
        if indegree[i] == 0: # 진입 차수가 0이 되면 dq에 넣는다.
            dq.append(i)

print(max(time))
    
