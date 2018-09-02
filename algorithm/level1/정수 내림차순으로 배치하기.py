def solution(n):
    answer = ""
    n_list = [int(x) for x in str(n)]
    n_list.sort(reverse = True)
    for i in n_list:
        answer += str(i)

    return int(answer)
