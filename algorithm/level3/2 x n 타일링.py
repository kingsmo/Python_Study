def solution(n):
    #이거 먼가 점화식으로 하면 풀릴거 같은데
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b % 1000000007
