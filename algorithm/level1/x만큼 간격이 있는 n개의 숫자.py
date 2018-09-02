def solution(x, n):
    answer = []
    plus = x
    for i in range(n):
        answer.append(x)
        x += plus
    return answer
