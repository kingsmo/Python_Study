def solution(s):
    answer = ""
    answer_list = []

    s_list = s.lower().split(' ')

    #한단어씩
    for i in s_list:
        #단어에서 글자마다 홀수
        oneWord = ''
        for index, j in enumerate(i):
            if index % 2 == 0:
                oneWord += j.upper()
            else:
                oneWord += j
        answer_list.append(oneWord)
    answer = ' '.join(answer_list)
    return answer
