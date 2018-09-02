def solution(n, s):

    if n > s:
        return [-1]

    answer = []

    #몫을 일단 초기값으로 놔둔다
    for i in range(n):
        answer.append(s//n)
    # 나머지만큼 남은값에 더해줘야 한다.
    addingNumber = s%n
    while addingNumber>0:
        for i in range(n):
            if addingNumber>0:
                answer[i]+=1
                addingNumber -= 1
            else:
                break
    return sorted(answer)
