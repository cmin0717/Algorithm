n = input()

if len(n) == 1: # n이 1자리면 0을 붙혀서 저장
    n = '0' + n

cnt = 0

def test(x):
    global cnt

    check = str(sum([int(i) for i in x])) # 입력받은 x값의 각 자리를 더해서 다시 문자형

    cnt += 1 

    new = x[-1] + check[-1] # 새로운 숫자 생성
    if new == n:
        return

    test(x[-1] + check[-1]) # 같은 수가 될때까지 반복

test(n)
print(cnt)
