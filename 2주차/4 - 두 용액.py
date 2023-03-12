import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int,input().split()))
solution.sort()

left = 0 # 좌측 끝이니깐 0
right = n-1 # 우측 끝 인덱스니깐 n-1

sum_num = abs(solution[left] + solution[right]) # 처음 설정값
result = [solution[left], solution[right]]

while left < right:
    left_num = solution[left]
    right_num = solution[right]
    x = left_num + right_num

    if abs(x) < sum_num: # 새로운 값이 설정값보다 0에 가까우면 재설정
        sum_num = abs(x)
        result = [left_num, right_num]
        if x == 0:
            break
    if x > 0: # x의 값에 따라 좌측, 우측의 좌표를 다시 설정한다.
        right -= 1
    else:
        left += 1

print(*result)

# 투포인터 문제이다. 보통 절대값이 비슷한 음수와 양수를 
# 합쳐야 0과 가까운 수가 나오므로 배열을 정렬한 후 양쪽 끝에서부터 비교해나가면 되는 문제다.
