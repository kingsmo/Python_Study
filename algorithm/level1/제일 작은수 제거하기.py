def solution(arr):
    answer = []
    if (not arr) or (len(arr) == 1) :
        return [-1]
    else:
        a = min(arr)
        arr.remove(a)
    answer = arr
    return answer
