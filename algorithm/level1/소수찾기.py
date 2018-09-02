
def solution(n):
    primes = []
    if n < 2:
        return primes
    for i in range(2, n+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return len(primes)
