def solution(n):
    answer = 0
    n_list = [int(x) for x in str(n)]
    for i in n_list:
        answer += i
    return answer
