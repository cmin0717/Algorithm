n = int(input())
word = list(input())

check = [str(i) for i in range(10)]

check_num = ''

for i in word:
    if i not in set(check): # i가 숫자인지 문자인지 파악
        check_num += ' ' # 문자라면 ' '빈칸을 넣어준다. 나중에 ' '으로 split해야함으로
    else:
        check_num += i #숫자면 숫자를 넣어준다.

hidden_nums = list(map(int, check_num.split())) # map과 split함수를 이용하여 문장에서 문자형 숫자를 int형으로 데려온다.
nums = [i for i in hidden_nums if len(str(i)) < 7] # 7자리 이하의 히든 넘버만 nums에 저장해준다.
print(sum(nums))

#
# for i in range(n):
#     if word[i] in check:
#         check_num += word[i]
#         if word[i+1] not in check:
#             hidden_num.append(int(check_num))
#             check_num = ''

# nums = [i for i in hidden_num if len(str(i)) < 7]
# print(sum(nums))

