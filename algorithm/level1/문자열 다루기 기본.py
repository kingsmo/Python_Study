# return s.isdigit() and len(s) in (4, 6)
def solution(s):
    if(len(s) == 4 or len(s) == 6):
        for i in s:
            if i.isdigit():
                pass
            else:
                return False
        return True

    else:
        return False
