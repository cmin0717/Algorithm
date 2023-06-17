from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

word = input().rstrip()

# 마지막에 식을 계산하는 함수
def calculation(word):
    q = deque(word)
    count = 0

    while q:

        num = q.popleft()

        if num == '+':
            count += int(q.popleft())
        elif num == '-':
            count -= int(q.popleft())
        elif num == '*':
            count = count * int(q.popleft())
        else:
            count += int(num)
    return count

# 추가한 괄호가 올바른 괄호인지 판단
def check(arr):
    for i in range(1, len(arr)):
        # 연속된 괄호는 올바른 괄호가 아니다.
        if arr[i] - arr[i-1] == 2:
            return False
    return True

# 괄호를 미리 계산하고 '' 값 처리
def drop(word):
    q = deque(word)
    s = []
    while q:
        num = q.popleft()
        if num:
            s.append(num)
    return s

# 괄호안의 값을 미리 계산후 나머지는 사용한 숫자는 ''값으로 변환
def trans(word, s):
    word = list(word)
    for i in s:
        if word[i] == '+':
            word[i] = str(int(word[i-1]) + int(word[i+1]))
        elif word[i] == '-':
            word[i] = str(int(word[i-1]) - int(word[i+1]))
        else:
            word[i] = str(int(word[i-1]) * int(word[i+1]))
        word[i-1], word[i+1] = '',''

    return calculation(drop(word))
    
arr = [i for i in range(1,n,2)]
result = calculation(word)
for i in range(1, ((n//2)//2)+2):
    # 조합을 사용하여 나올수있는 괄호의 위치를 구함
    for s in combinations(arr, i):
        if not check(s):
            continue
        result = max(result, trans(word, s))

print(result)
