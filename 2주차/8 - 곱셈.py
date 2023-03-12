import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def test(x, y):
    if y == 0: # y가 0일 경우에는 1 리턴
        return 1
    if y % 2 == 0: # 2로 나누어 떨어진다면 n//2을 제곱 해주고 % c 해서 리턴
        n = test(x, y//2) % c # 이렇게 쭉 분할해서 해결하면 o(n)에서 o(logn)까지 줄일수있다.
        return n * n
    else:
        return x * test(x,y-1) % c  # 홀수라면 n-1 * x % c해서 리턴

# a**b % c 의 값과 아래 결과값은 결국 같다.(모듈러의 연산의 성질)
print(test(a,b) % c) # test(a,b)에서 나온값을 다시 c로 나누어 리턴


# 모듈러의 연산의 성질
# 곱하고 나머지를 구하나 나머지끼리 곱하고 다시 나머지를 구하나 값은 같다.
# 원리가 그렇다니깐 이해하자....
# 1. (a+b) mod n = [(a mod n)+(b mod n)] mod n 

# 2. (a*b) mod n = [(a mod n)*(b mod n)] mod n