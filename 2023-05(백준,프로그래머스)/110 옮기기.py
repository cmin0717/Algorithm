def solution(s):
    
    result = []

    for word in s:

        rest = []
        cnt_110 = 0

        # 문자열을 돌면서 완성되는 110을 다 뺴주고 개수를 구한다.
        for w in word:
            if len(rest) >= 2 and rest[-2] == '1' and rest[-1] == '1' and w == '0':
                cnt_110 += 1
                rest.pop()
                rest.pop()
            else:
                rest.append(w)
        
        cnt_1 = 0
        # 110이 빠진 문자열에서 역순으로 조회할때 0이 나올때까지 조회한다.
        for i in range(len(rest)-1, -1, -1):
            if rest[i] == '0':
                break
            else:
                cnt_1 += 1
        # 110이 빠진 문자열에서 0이 나오기전까지 나온 1의 개수와 110의 개수를 이용하여 최종 문자열을 구한다.
        new_word = ''.join(rest[:len(rest)-cnt_1]) + '110' * cnt_110 + '1' * cnt_1
        result.append(new_word)
    
    return result

solution(	["1110", "100111100", "0111111010"])