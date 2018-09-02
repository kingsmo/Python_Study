def solution(s):
    answer = ''
    #홀수
    if len(s) % 2 == 1:
        index = int(len(s)/2)
        answer = s[index]
    elif len(s) % 2 == 0:
        index = int(len(s)/2)
        answer = s[index-1:index+1]



    return answer
