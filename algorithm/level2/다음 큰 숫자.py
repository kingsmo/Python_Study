def solution(n):
    answer = 0
    number = bin(n)
    #숫자 카운트
    count_a = str(number)[2:].count('1')
    while True:
        n += 1
        # 넘버를 1씩 증가시키며 1의개수가 같은지 확인해서 같으면 리턴
        count_b = str(bin(n))[2:].count('1')
        if count_a == count_b:
            break
    return n
