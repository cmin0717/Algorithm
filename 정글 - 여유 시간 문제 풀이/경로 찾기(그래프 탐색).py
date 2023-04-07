import sys
input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n)]
result = [[0] * n for _ in range(n)]

# 단방향 간선이므로 한쪽으로만 연결리스트 생성
for i in range(n):
    line = list(map(int,input().split()))
    for j in range(n):
        if line[j] == 1:
            link[i].append(j)

# dfs을 이용하여 해당 정점에서 갈 수 있는 정점을 1로 변환
def check(std,idx):
    for i in link[idx]:
        if result[std][i] == 0:
            result[std][i] = 1
            check(std,i)
    return result[std] # 리턴값으로 완성된 해당 정점을 리턴 / 어차피 마지막 리턴값만 있으면 되니깐 재귀의 조건을 주지 않았다.

for i in range(n):
    print(*check(i,i))