from collections import deque

n = int(input())

time = [0]
degree = [0] * (n+1)
li = [[] for _ in range(n+1)] # 진입 차수에 대한 정보가 있는 연결리스트
li2 = [[] for _ in range(n+1)] # 건물을 올리는데 필요한 시간을 구하기 위한 연결리스트
dq = deque()

for i in range(n):
    info = list(map(int,input().split()))
    if len(info) == 2: # info의 원소가 2개밖에 없다면 진입차수가 0인 아이들이다.
        time.append(info[0])
        dq.append(i+1)
    else:
        time.append(info[0])
        for j in range(1,len(info)-1): # 해당 건물을 짓는데 필요한 건물을 여러개 줄수도있다.
            li[info[j]].append(i+1)
            li2[i+1].append(info[j])
            degree[i+1] += 1

while dq:
    idx = dq.popleft()
    
    if len(li2[idx]) != 0:
        check = []
        for i in li2[idx]:
            check.append(time[i])
        time[idx] = max(check) + time[idx]

    for j in li[idx]:
        degree[j] -= 1
        if degree[j] == 0:
            dq.append(j)

print(*time[1:],sep='\n')
