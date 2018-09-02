def solution(arr):
        a = []
        for i in arr:
            print(a[-1:], [i])
            if a[-1:] == [i]:
                continue
            a.append(i)
        return a
