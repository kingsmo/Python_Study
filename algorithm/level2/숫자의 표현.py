def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp_sum = 0
        a = i
        while True:
            temp_sum += a
            if temp_sum > n:
                break
            elif temp_sum == n:
                answer+= 1
                break
            a += 1
    return answer
