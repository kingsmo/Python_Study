def solution(s):
    answer = 0
    result = []

    for i in range(len(s)):

        for j in range(1,len(s)+1):

            if s[i:j] and str(s[i:j]) == str(s[i:j])[::-1]:

                result.append(len(s[i:j]))

            if s[j:i] and str(s[j:i]) == str(s[j:i])[::-1]:

                result.append(len(s[j:i]))

    return max(result)

    # 한글자씩 확인
    for i in range(len(s)):
        #확인해야 할 길이가 일단 짝수인지 먼저 확인
        if (len(s) - i) % 2 == 0 or i > len(s) - 3:
            continue
        #팰린드롬인지 확인
        index = 0
        for j in range(i, (len(s) - i)//2 ):
            if s[j+index] == s[len(s)-1-index]:
                print(s[j+index])
                index += 1
        if index > answer:
            answer = index*2 + 1
    return answer
