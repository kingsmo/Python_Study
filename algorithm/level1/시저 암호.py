def solution(s, n):
    answer = ''
    for k in s:
        #알파벳인지 먼저 확인
        if k.isalpha():
            #소문자 대문자인지 확인
            if k.islower():
                answer += chr((ord(k) - ord("a") + n) % 26 + ord("a"))
            else:
                answer += chr((ord(k) - ord("A") + n) % 26 + ord("A"))
        else:
            answer += k
    return answer
