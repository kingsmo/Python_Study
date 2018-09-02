def solution(s):
    answer = ""
    n_list = s.split()
    for i in range(len(n_list)):
        n_list[i] = int(n_list[i])
    n_list.sort()
    answer += (str(n_list[0]))
    answer = answer + " "+ (str(n_list[-1]))
    return answer
