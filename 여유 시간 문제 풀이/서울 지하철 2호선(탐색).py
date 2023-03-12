from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

link = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 연결된 노선을 진입차수로 본다.
no_cycle = deque([])

for _ in range(n):
    x,y = map(int,input().split())
    link[x].append(y)
    link[y].append(x)
    indegree[x] += 1
    indegree[y] += 1

for i in range(1,n+1):
    if indegree[i] == 1: # 진입 차수가 1이면 연결된 노선이 1개밖에 없으니 순환역이 될수없다.
        no_cycle.append(i)

while no_cycle: # 진입 차수를 이용하여 순환역 말고는 진입 차수를 다 0으로 만든다.
    idx = no_cycle.popleft()
    if indegree[idx] > 0:
        indegree[idx] -= 1
    
    for i in link[idx]:
        if indegree[i] > 0:
            indegree[i] -= 1
        if indegree[i] == 1:
            no_cycle.append(i)

def check(idx,cnt): # 순환역에서 최소거리가 얼마인지 구하는 함수
    for i in link[idx]:
        if indegree[i] == 0 and terminal[i] > cnt: # 진입 차수가 0이고 현재 거리가 cnt보다 멀 경우
            terminal[i] = cnt
            check(i, cnt+1)

terminal = [3001] * (n+1) # 초기값 설정
for i in range(1,n+1):
    if indegree[i] != 0: # 진입 차수가 0이 아니라면 순환역이다.
        check(i,1)
        terminal[i] = 0
print(*terminal[1:])



