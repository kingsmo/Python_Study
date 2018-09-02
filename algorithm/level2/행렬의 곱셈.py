def solution(A, B):
    answer = [ len(B[0])*[0] for i in range (len(A)) ]
    for i in range (len(answer) ):
        for j in range ( len(answer[i]) ):
            for k in range ( len(A[i] ) ):
                answer[i][j] += A[i][k]*B[k][j]

    return answer
