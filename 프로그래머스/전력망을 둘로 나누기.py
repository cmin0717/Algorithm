# 얕은 카피를 이용한 풀이
def check(arr):
    node = [i for i in range(len(arr))]
    def dfs(arr, idx):
        for i in arr[idx]:
            if node[idx] != node[i]:
                node[i] = node[idx]
                dfs(arr,i)
    for i in range(1,len(arr)):
        dfs(arr,i)
    num = [node.count(i) for i in list(set(node[1:]))]
    return abs(num[0]-num[1])

def solution(n, wires):
    link = [[] for _ in range(n+1)]

    for x,y in wires:
        link[x].append(y)
        link[y].append(x)

    result = n
    for x,y in wires:
        # arr = deepcopy(link)
        # arr[x].remove(y)
        # arr[y].remove(x)
        # 얕은 복사를 할 경우 재할당시에는 문제가 없지만 위처럼 값을 변경할때는 원본에 영향을 준다.
        arr = link[:]
        arr[x] = [i for i in arr[x] if i != y]
        arr[y] = [i for i in arr[y] if i != x]
        result = min(result,check(arr))

    return result
print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))