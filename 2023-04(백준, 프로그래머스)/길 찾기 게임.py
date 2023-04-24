import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodeinfo = [nodeinfo[i]+[i+1] for i in range(len(nodeinfo))] # 노드의 번호를 추가로 입력해준다.
    arr_y = sorted(nodeinfo, key=lambda x:-x[1]) # y를 기준으로 정렬 내림차순으로
    
    return prepos(arr_y,[],[]) # 정렬된 배열과 결과를 담을 두개의 리스트를 인자로 넣어준다.

def prepos(arr_y, arr1,arr2):
    root = arr_y[0] # 정렬시켰으므로 0번째가 루트가 된다.
    left = []
    right = []
    
    for i in range(1,len(arr_y)): # 배열을 돌면서 루트의 왼쪽 자식 오른쪽 자식을 구한다.
        if arr_y[i][0] < root[0]:
            left.append(arr_y[i])
        else:
            right.append(arr_y[i])
            
    arr1.append(root[2]) # 전위순회값
    if left:
        prepos(left, arr1,arr2) # 왼쪽 자식이 존재한다면 진행 (정렬시킨상태로 for문을 돌았으므로 해당 자식들도 정렬된 상태이다.)
    if right:
        prepos(right,arr1,arr2)
    arr2.append(root[2]) # 후위순회값
    return arr1,arr2

# 직접 트리를 만들라고 썡쇼를 했다.....
# 이렇게 간단한 문제였는데 루트를 구하고 나누고 나눈 것중에 다시 루트를 구하고 나누고 하면 금방 찾을수있다.

solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])