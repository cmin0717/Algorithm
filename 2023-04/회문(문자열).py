import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def check(s,e,c):
    global result

    # 조건에 따라 종료시점을 설정
    if s >= e:
        result = min(result,c)
        return
    if c == 2:
        result = min(result,c)
        return
    
    # 계속 재귀로 들어가면 리커젼 오류가 발생하기에 회문이 되는곳까지는 for문을 통해 진행
    if word[s] == word[e]:
        for i in range(e+1//2):
            if word[s+i] != word[e-i]:
                check(s+i,e-i,c)
                return
        else:
            result = c
            return
    
    # 유사회문 판단
    if word[s+1] == word[e]:
        check(s+2,e-1,c+1)
    if word[s] == word[e-1]:
        check(s+1,e-2,c+1)

for _ in range(n):
    word = input().rstrip()
    s,e = 0, len(word)-1 # 시작과 끝점을 정한다.
    result = 2 # 디폴트값으로 2삽입
    check(s,e,0)
    print(result)
    
