def solution(word):
    alpha = ['A','E','I','O','U']
    cnt = 0
    for a in alpha:
        result = a
        cnt += 1
        if result == word : return cnt
        for b in alpha:
            result = a+b
            cnt += 1
            if result == word : return cnt 
            for c in alpha:
                result = a+b+c
                cnt += 1
                if result == word : return cnt
                for d in alpha:
                    result = a+b+c+d
                    cnt += 1
                    if result == word : return cnt
                    for e in alpha:
                        result = a+b+c+d+e
                        cnt += 1
                        if result == word : return cnt
solution("A")
# 이게 맞나??ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# 공식을 구하면 쉽게 할수있지만 패쓰!!
# 중복 순열로 구현할수있지만 코드는 더럽지만 이게 훨씬 효율적일듯