# return s.lower().count('p') == s.lower().count('y')
def solution(s):
    answer = True

    count_p = 0
    count_y = 0

    for i in range(len(s)):
        if (s[i] == 'p' or s[i] == 'P'):
            count_p += 1
        elif (s[i] == 'y' or s[i] == 'Y'):
            count_y += 1
    if(count_p == 0 and count_y == 0):
        return False
    elif (count_p == count_y):
        return True
    else:
        return False
