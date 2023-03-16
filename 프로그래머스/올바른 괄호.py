def solution(s):
    check = 0
    for i in s:
        if i == '(':
            check += 1
        elif i == ')':
            if check > 0:
                check -= 1
            else:
                return False
    return check == 0
    