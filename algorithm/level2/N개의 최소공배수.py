def solution(arr):
    answer = 0
    arr.sort()
    a = max(arr)
    result = False
    while True:
        for i, value in enumerate(arr):
            if a % value != 0:
                a += 1
                break
            elif i == len(arr) -1:
                result = True
                break
        if result == True:
            break


    return a
