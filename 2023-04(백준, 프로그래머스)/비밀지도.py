def solution(n, arr1, arr2):
    
    result = []
    
    for i in range(n):
        x = int(bin(arr1[i])[2:])
        y = int(bin(arr2[i])[2:])
        result.append(str(x+y))
    
    for i in range(n):
        check = ''
        for j in result[i]:
            check += ' ' if j == '0' else '#'
        result[i] = ' '*(n-len(check)) + check
    
    return result