def solution(str1, str2):
    str1,str2 = str1.upper(), str2.upper() # 대소문자 구분이 없기에 대문자로 통일
    if str1 == str2: return 65536 # 만일 처음부터 둘이 같다면 바로 종료

    s1,s2 = [],[]
    dic = {} # 알파벳인지 확인하기 위해
    for i in range(26):
        dic[chr(i+65)] = 1
    
    # 각 문자열을 조건에 맞게 파싱
    for i in range(1,len(str1)):
        if str1[i] in dic and str1[i-1] in dic:
            s1.append(str1[i-1]+str1[i])
    for i in range(1,len(str2)):
        if str2[i] in dic and str2[i-1] in dic:
            s2.append(str2[i-1]+str2[i])
    
    cnt = 0
    visit1, visit2 = set(),set() #각각 따로 방문체크를 한다.

    # 2중 for문을 돌면서 교집합을 구함(방문 체크를 함으로 중복 제거)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and i not in visit1 and j not in visit2:
                cnt += 1
                visit1.add(i)
                visit2.add(j)
                
    union = len(s1) + len(s2) - cnt
    return int((cnt/union)*65536)