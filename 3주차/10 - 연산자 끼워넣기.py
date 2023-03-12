n = int(input())

nums = list(map(int,input().split()))

add, sub, mul, div = map(int,input().split())
result = []

def operator(cnt, operand, m, add, sub, mul, div): # 함수에 연산횟수, 현재값, 다음값의 인덱스, 덧셈수, 뺄셈수, 곱셈수, 나눗셈수를 넣어준다. 
    if cnt == n-1: # 연산횟수가 n-1개면 끝난거니깐 result에 넣어준다. 
        result.append(operand)
        return
    if add > 0:
        operator(cnt+1, operand+nums[m], m+1, add-1, sub, mul, div)
    if sub > 0:
        operator(cnt+1, operand-nums[m], m+1, add, sub-1, mul, div)
    if mul > 0:
        operator(cnt+1, operand*nums[m], m+1, add, sub, mul-1, div)
    if div > 0:
        operator(cnt+1, int(operand/nums[m]), m+1, add, sub, mul, div-1) # 음수가 올수도 있기에 //(몫)으로 하면 안된다. /은 실수형으로 나오니깐 int변환

operator(0,nums[0],1,add,sub,mul,div)
print(max(result),min(result),sep='\n')