from functools import cmp_to_key

def solution(num):
    num = [str(i) for i in num]
    
    def check(x,y):
        if x+y >= y+x:
            return -1
        else:
            return 1
    
    num.sort(key=cmp_to_key(check))
    result = ''
    for i in num:
        result += i
        
    if result[0] == '0':
        result = '0'
    return result
# cmp_to_key라이브러리를 사용하여 커스텀 정렬을 만들수 있다.