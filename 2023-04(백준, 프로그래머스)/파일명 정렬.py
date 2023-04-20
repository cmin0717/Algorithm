def solution(files):
    dic = {}
    check = set(str(i) for i in range(10))
    
    for file in files: # 입력 받은 파일을 헤더와 넘버, 꼬리로 나눈다.
        head,num = '',''
        h,n = True,True
        for f in file:
            if f in check:
                h = False
            if not h and f not in check:
                n = False
            if h:
                head += f
            elif n:
                num += f
            else:
                break # 꼬리는 필요없으니 바로 종료

        head,num = head.upper(), int(num) # 나눈 헤더와 넘버를 대문자, 숫자형으로 통일

        # 딕셔너리로 헤더와 넘버로 기준을 나누어 들어온 순서대로 모아둔다. 저장시에는 원본명으로 저장
        if dic.get(head) == None: 
            dic[head] = {}
            dic[head][num] = [file]
        elif dic[head].get(num) == None:
            dic[head][num] = [file]
        else:
            dic[head][num].append(file)

    result = []
    
    for key in sorted(dic.keys()): # 헤더순으로 키값을 정렬시켜서 가져온다.
        for v_key in sorted(dic[key].keys()): # 헤더안에서 넘버값을 정렬시켜서 가져온다.
            for value in dic[key][v_key]: # 그렇게 가져온 값을 안에 있는 순서대로 담는다.
                result.append(value)
    return result
        
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])