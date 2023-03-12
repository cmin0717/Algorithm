from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

degree = [0] * (n+1) # 진입 차수를 넣어두는 곳

student = [[] for _ in range(n+1)] # 입력 받은 값의 연결 리스트 생성
for _ in range(m):
    x,y = map(int,input().split())
    student[x].append(y) # 단반향이니깐 한쪽으로만 저장
    degree[y] += 1 # 연결리스트를 저장하면서 진입 차수도 같이 저장한다.

dq = deque()
for i in range(1,n+1): # 처음 시작할 진입차수가 0인 노드들을 미리 큐에 넣어준다.
    if degree[i] == 0:
        dq.append(i)

result = [] # 위상 정렬 결과를 넣어둘 장소
while dq:
    stu = dq.popleft() 
    result.append(stu) # pop된 순서로 result리스트에 저장한다.
    for i in student[stu]:
        degree[i] -= 1 # pop된 노드와 연결된 노드들의 진입 차수를 -1 씩 해준다.
        if degree[i] == 0: # 진입 차수가 0이 되었다면 큐에 넣어준다.
            dq.append(i)

print(*result)