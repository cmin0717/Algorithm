import sys
input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(int(n))]
# set자료형을 이용하여 중복값 제거
words = set(words)

# sorted() 함수의 키값에 길이,사전순을 정해주어 풀어보았다.
# 기본 sort()함수는 알아서 사전순으로 해주기에 그냥 x값을 넣어주었다.
words = sorted(words, key=lambda x : (len(x), x))
print(*words, sep='\n')
