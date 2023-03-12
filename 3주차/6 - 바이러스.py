n = int(input())
m = int(input())
# 연결 리스트? 뭐 그걸로 풀어본 풀이 (로직은 아래 풀이와 거의 같다)

com = [[] for _ in range(n+1)] # 컴터 수만큼 리스트를 만듬
virus = [0] * (n+1)

for _ in range(m):
    x,y = map(int,input().split()) # 네트워크를 입력 받고 각 컴퓨터 리스트에 서로 연결된 네트워크를 넣어준다.
    com[x].append(y)
    com[y].append(x)

def check(x):
    virus[x] = 1
    for i in com[x]:
        if virus[i] == 0: # 연결된 네트워크가 아직 바이러스에 감염이 안되었다면 바이러스를 넣어준다.
            check(i)

check(1)
print(sum(virus)-1)


# 딕셔너리를 이용해서 풀어본 풀이
# network = {}
# virus = []

# for i in range(m):
#     num = list(map(int,input().split()))
#     num.sort()
#     if network.get(num[0]) == None:
#         network[num[0]] = [num[1]]
#     else:
#         network[num[0]] = [num[1]] + network.get(num[0])
#     if network.get(num[1]) == None:
#         network[num[1]] = [num[0]]
#     else:
#         network[num[1]] = [num[0]] + network.get(num[1])

# def check(x):
#     virus.append(x)
#     if x in network.keys():
#         for i in network[x]:
#             if i not in set(virus):
#                 check(i)

# check(1)
# print(len(set(virus))-1)