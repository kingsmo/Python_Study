def solution(phone_number):
    star = '*'
    answer = star * (len(phone_number) - 4)
    answer += phone_number[-4:]
    return answer
