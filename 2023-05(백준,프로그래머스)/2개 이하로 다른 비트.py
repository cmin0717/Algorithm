def solution(numbers):
    
    result = []
    
    for num in numbers:
        # 10진수를 2진수로 변환
        bin_num = [n for n in bin(num)[2:]]
        # 수정만 해야하는지 추가를 해야하는지 판단하기 위한 변수들
        play,check = True, 0

        # 2진수를 뒤에서부터 보면서 0이 있다면 1로 바꾸어주고 스탑
        for i in range(len(bin_num)-1,-1,-1):
            if bin_num[i] == '0':
                bin_num[i] = '1'
                play, check = False, i
                break
        # 위의 과정에서 값이 변했다면 바꾼 값의 위치부터 맨뒤까지 보면서 1이 있다면 0으로 바꾸어주고 스탑!
        if not play:
            for i in range(check+1, len(bin_num)):
                if bin_num[i] == '1':
                    bin_num[i] = '0'
                    break
        # 위의 과정을 하나도 거치지 않았다면 현재 이진수는 1로만 이루어진 2진수이니깐 0번째 인덱스를 0으로 바꾸고 맨앞에 1을 추가해준다.
        else:
            bin_num[0] = '0'
            bin_num = ['1'] + bin_num
        
        # 2진수를 다시 10진수로 변환후 값 저장
        bin_num = ''.join(['0b'] + bin_num)
        result.append(int(bin_num, 2))
    
    return result