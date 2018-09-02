from fractions import gcd
def solution(n, m):
    answer = []
    return [gcd(n,m), n*m/gcd(n,m)]
