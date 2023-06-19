import sys
input = sys.stdin.readline

need = int(input())

n,m = map(int, input().split())

left = [int(input()) for _ in range(n)]
right = [int(input()) for _ in range(m)]

# 각 피자의 부분합의 경우의수를 딕셔너리에 저장
def findsum(size, arr, dic):
    for i in range(size):
        tt = arr[i]
        dic.setdefault(tt, 0)
        dic[tt] += 1
        for j in range(1, size-1):
            tt += arr[(i+j) % size]
            if tt > need: 
                break
            dic.setdefault(tt, 0)
            dic[tt] += 1

    # 합이 0과 총합은 1가지의 경우의수만 나오니깐 1로 설정
    dic[0] = 1
    dic[sum(arr)] = 1
    return dic

sum_left, sum_right = findsum(n, left, {}), findsum(m, right, {})

# 필요한 피자를 얻을수있는 모든 경우의 수
result = 0
for i in range(need+1):
    if i in sum_left and need-i in sum_right:
        result += sum_left[i] * sum_right[need-i]
print(result)