import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = []
    for i in input().rstrip(): # 각 문자가 연달아 나오면 하나만 word에 저장
        if len(word) == 0:
            word.append(i)
            continue
        if i != word[-1]:
            word.append(i)

    if len(word) > 5: # 위에서 구한 word가 5자리가 넘어가면 규칙을 만족할수없다.
        print('Good')
        continue
    
    if 'AFC' in ''.join(word) and word[-1] in ['A', 'B', 'C', 'D', 'E', 'F']: # 규칙을 만족했다면 infected출력
        print("Infected!")
    else:
        print('Good')
