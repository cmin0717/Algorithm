import sys
input = sys.stdin.readline

n = int(input())
s,e = input().rstrip().split('*') # *기준으로 시작 문자와 끝 문자로 나누어준다.

words = [input().rstrip() for _ in range(n)]

for word in words:
    if len(word) < len(s) + len(e): # 만일 패턴의 길이가 주어진 문자열 보다 길다면 실패
        print('NE')
        continue
    if word[:len(s)] == s and word[-len(e):] == e: # 패턴의 시작과 끝이 단어의 시작과 끝과 같다면 DA출력
        print('DA')
    else:
        print('NE')
