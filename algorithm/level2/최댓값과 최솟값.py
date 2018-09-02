def solution(s):
    array = []
    for i in s:
        if i == "(":
            array.append(i)
        elif i == ")":
            #어레이가 비어있으면
            if not array:
                return False
            else:
                array.pop()
    if not array:
        return True
    else:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     answer = True
#     print('Hello Python')
#     arr = []
#     if(s[0] == ')' or s[len(s)-1] == '('):
#         return False

#     for i in range(len(s)):
#         if(s[i] == '('):
#             arr.append('(')
#         elif(s[i] == ')'):
#             if not arr:
#                 return False
#             else:
#                 arr.pop()
#     return answer
