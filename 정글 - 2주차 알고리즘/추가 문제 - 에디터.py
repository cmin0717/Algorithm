import sys
input = sys.stdin.readline

word = [i for i in input().rstrip()] 
word2 = [] # 커서를 기준으로 좌.우로 나누어 저장

n = int(input())

cursor = len(word) # 커서는 글자의 길이 만큼

commend = [list(input().rstrip().split()) for _ in range(n)]

for i in commend:
    if i[0] == 'L':
        if cursor == 0:
            continue
        else:
            cursor -= 1 # 커서를 왼쪽으로 이동하면 커서 기준으로 다시 글자를 나눈다.
            word2.append(word.pop())
    elif i[0] == 'D':
        if cursor == len(word) + len(word2):
            continue
        else:
            cursor += 1 # 위와 같이 커서를 기준으로 글자를 나눈다.
            word.append(word2.pop())
    elif i[0] == 'B':
        if cursor == 0:
            continue
        else:
            word.pop() # 커서 기준 왼쪽을 지우니깐 word쪽에서 pop
            cursor -= 1
    else:
        word.append(i[1]) # 커서 기준 왼쪽에 추가니간 word쪽에 append
        cursor += 1

word2.reverse() # 커서 기준 우측은 반대로 저장되었기에 reverse해준다.
print(''.join(word + word2))