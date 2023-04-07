import sys
input = sys.stdin.readline

word = input().rstrip()

for i in range(len(word)//4+1,0,-1): # 길이가 큰것부터 제거해야 예외처리가 발생하지 않는다.(wwwolfoollff같은 상황)
    if len(word) == 0: break
    check = ''.join([j*i for j in 'wolf'])
    word = ''.join(word.split(check))

if len(word) == 0:
    print(1)
else:
    print(0)
