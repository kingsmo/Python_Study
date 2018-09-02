def solution(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += i

    answer = sum_arr / len(arr)
    return answer
