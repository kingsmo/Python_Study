def solution(x):
    n_list = [int(x) for x in str(x)]
    if x % sum(n_list) == 0 :
        return True
    else:
        return False
