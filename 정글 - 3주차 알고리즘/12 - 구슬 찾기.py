import sys
input = sys.stdin.readline

n,m = map(int,input().split())

heavy = [[] for _ in range(n+1)] # 무거운 애들을 기준으로 연결리스트를 만든다.
light = [[] for _ in range(n+1)] # 가벼운 애들을 기준으로 연결리스트를 만든다.

for _ in range(m):
    x,y = map(int,input().split())
    if x not in set(heavy[y]): # 중복된 값이 없다면 넣어준다.
        heavy[y].append(x)
    if y not in set(light[x]):
        light[x].append(y)

def dfs(x,arr):
    global cnt
    if cnt >= (n+1)//2: # 만일 cnt가 이미 구슬 수의 반절을 넘어 갔다면 더 이상 진행할 의미가 없다.
        return
    for i in arr[x]:
        if check[i] == 0: # 방문 체크 해주고
            cnt += 1
            check[i] = 1
            dfs(i,arr) # 다시 재귀

result = 0
for i in range(1,n+1):
    check = [0] * (n+1) # 무거운 애들, 가벼운 애들 둘다 확인해 주어야한다.
    cnt = 0
    check[i] = 1
    dfs(i,heavy)
    if cnt >= (n+1)//2:
        result += 1
    check = [0] * (n+1)   
    check[i] = 1 
    cnt = 0
    dfs(i, light)
    if cnt >= (n+1)//2:
        result += 1

print(result)