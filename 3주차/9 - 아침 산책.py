import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
in_out = '0' + input().rstrip()
link = [[] for _ in range(n+1)]
count = 0

for _ in range(n-1):
    x,y = map(int,input().split())
    link[x].append(y)
    link[y].append(x)
    if in_out[x] == in_out[y] == '1': # 둘다 실내이면 미리값을 넣어준다.
        count += 2

def dfs(x):
    global cnt
    check[x] = 1
    for i in link[x]:
        if in_out[i] == '1': # 실내니깐 +1 해준다.
            cnt += 1
        elif check[i] == 0 and in_out[i] == '0': # 연결가능한 실외가 나온다면 dfs로 재귀해준다.
            dfs(i)
    return

check = [0] * (n+1)
for i in range(1,n+1):
    cnt = 0
    if check[i] == 0 and in_out[i] == '0': # 실외일때만 dfs에 들어간다.
        dfs(i)
        count += cnt * (cnt-1)

print(count)

# 결국 실외에 연결된 실내 중에 2개를 고르는 문제이다.
# 실외가 서로 연결되어있으면 총 연결된 실내 수 * (실내 수 -1)해주면 된다.



# 73점 짜리 코드
# for x,y in line:
#     li[x].append(y)
#     li[y].append(x)

# for i in range(len(a)):
#     li[i+1].append(a[i]) # 실내인지 실외인지 각 노드별로 넣어준다.

# def dfs(x):
#     global cnt
#     check[x] = 1
#     for i in li[x][:-1]:
#         if li[i][-1] == '1' and check[i] == 0: # 가는곳이 실내라면 종료
#             cnt += 1 
#         else:
#             if check[i] == 0:
#                 dfs(i) # 실내가 아니라면 재귀함수로 더 들어간다.
#     return


# count = 0
# for i in range(1,n+1):
#     if li[i][-1] == '1': # 출발지가 실내인 곳을 다 해본다.
#         check = [0] * (n + 1)
#         cnt = 0
#         dfs(i)
#         count += cnt

# print(count)

# # 풀긴 했는데 73점 나옴ㅎㅎ 다른 조건 자체를 이해를 못해서 다음에 다음 조건까지 풀어보기로....