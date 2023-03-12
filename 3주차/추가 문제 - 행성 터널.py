from heapq import *
import sys
input = sys.stdin.readline
# 메모리 관리를 해야하는데 문제 부분을 이해를 잘 못하겠다... 포기!

n = int(input())

def star_cost(x,y):
    a = []
    for i in range(3):
        a.append(abs(x[i]-y[i]))
    return min(a)
star = [0]+ [list(map(int,input().split())) for _ in range(n)]

li = [[] for _ in range(n+1)]
check = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost = star_cost(star[i],star[j])
        li[i].append([cost,j])
        li[j].append([cost,i])

hq = []
heappush(hq,[0,1])

result = 0
while hq:
    cnt,idx = heappop(hq)

    if check[idx] == 0:
        check[idx] = 1
        result += cnt
        for c,x in li[idx]:
            if check[x] == 0:
                heappush(hq,[c,x])
print(result)


# kruskal로 해봣는데 메모리 초과가 나옴 

li = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        cost = star_cost(star[i],star[j])
        li.append([cost,i,j])
li.sort()

parents = [i for i in range(n+1)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    a = find(x)
    b = find(y)

    if a < b :
        parents[b] = a
    else:
        parents[a] = b

result = 0
for c,x,y in li:
    if find(x) != find(y):
        result += c
        union(x,y)
print(result)