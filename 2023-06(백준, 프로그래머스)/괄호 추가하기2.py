from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

word = input().rstrip()

def calculation(word):
    q = deque(word)
    s = []

    while q:

        num = q.popleft()

        if num == '*':
            s.append(str(int(s.pop()) * int(q.popleft())))
        else:
            s.append(num)
    
    q = deque(s)
    count = 0

    while q:

        num = q.popleft()

        if num == '+':
            count += int(q.popleft())
        elif num == '-':
            count -= int(q.popleft())
        else:
            count += int(num)
    return count

def check(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 2:
            return False
    return True

def drop(word):
    q = deque(word)
    s = []
    while q:
        num = q.popleft()
        if num:
            s.append(num)
    return s

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
    for s in combinations(arr, i):
        if not check(s):
            continue
        result = max(result, trans(word, s))

print(result)
