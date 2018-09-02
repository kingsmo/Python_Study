answer = [[]]

def solution(n):
    tower(n, 1, 3, 2)
    del answer[0]
    return answer

def tower(n, fro, to, tmp):
    if n > 1 :
        tower(n-1, fro, tmp, to)
        answer.append([fro, to])
        tower(n-1, tmp, to, fro)
    else :
        answer.append([fro, to])
