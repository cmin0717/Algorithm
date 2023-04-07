import sys
input = sys.stdin.readline

n = int(input())
muscle_loss = list(map(int,input().split()))
muscle_loss.sort()
result = []

if n % 2 == 0: # 머신이 짝수일 경우
    for i in range(n//2):
        x = muscle_loss[i] + muscle_loss[n -i -1]
        result.append(x)
else: # 머신이 홀수인 경우
    result.append(muscle_loss[-1]) # 마지막 1개는 미리 넣어주고 짝수 처럼 처리한다.
    for i in range((n-1)//2):
        x = muscle_loss[i] + muscle_loss[n -i -2]
        result.append(x)

print(max(result))
