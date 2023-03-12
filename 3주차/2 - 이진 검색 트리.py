import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nums = []

while True:
    try:
        num = int(input())
        nums.append(num)
    except: # 더이상 입력값이 없다면 break
        break


def dfs(start,end):
    if start > end:
        return
    check = end + 1 # 오른쪽 자식이 없을수 있기에 초기값을 end보다 크게 설정
    for i in range(start+1, end + 1):
        if nums[start] < nums[i]: # 루트보다 커지는 부분 즉, 오른쪽 자식이 시작하는부분
            check = i
            break
    dfs(start+1, check - 1) # 왼쪽 자식
    dfs(check,end) # 오른쪽 자식
    print(nums[start]) # 루트

dfs(0,len(nums)-1)

# 각 트리의 루트를 기준으로 오.자, 왼.자로 나눈다.
# 재귀적으로 계속 나누다가 자식이 없으면 출력