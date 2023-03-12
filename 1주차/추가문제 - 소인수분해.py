n = int(input())

num = 2

while num <= n**0.5:
    if n % num == 0:
        print(num)
        n = n // num
    else:
        num += 1

if n > 1 : print(n)

# 두 풀이의 차이점은 시작점을 전 끝점으로 하냐 마냐의 차이인듯.
# 전 끝점으로 시작을 해도 소인수분해에 영향이 없다.


# 재귀 함수로 풀어봄 (속도 650ms)
# def test(m):
#     if m == 1:
#         return
#     else:
#         for i in range(2,m+1):
#             if m % i == 0:
#                 print(i)
#                 return test(m//i)

# test(n)