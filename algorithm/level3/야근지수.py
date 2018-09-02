function solution(n, works) {
    for(let i = 0; i < n; i++) {
        works.sort((a,b) => b-a)
       if(works[0] > 0){
           --works[0]
       }else {
           return 0
       }
    }
    return works.reduce((acc, num) => acc + (num*num),0)
}

def solution(n, works):
    answer = 0
    for i in range(n):
        if(sum(works) <= 0):
            return 0

        # 다같을경우
        elif sum(works)/len(works) == works[0]:
            mok = (n - i - 1) // len(works)
            for j in range(mok):
                for k in range(len(works)):
                    works[k] = works[k] - 1
            i = i + mok * len(works)
            continue

        else:
            for index, value in enumerate(works):
                if value == max(works):
                    works[index] = value - 1
                    break


    for j in works:
        answer += j ** 2
    return answer
