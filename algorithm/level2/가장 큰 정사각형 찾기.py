def solution(board):
    answer = 1234
    lengthY = len(board)
    lengthX = len(board[0])
    a = 0
    if(lengthY < 2 or lengthY < 2):
        for i in range(lengthY):
            for j in range(lengthX):
                if board[i][j] == 1:
                    a = 1
    else:
        for i in range(1, lengthY):
            for j in range(1, lengthX):
                if board[i][j] == 1:
                    board[i][j] = min(board[i - 1][j], board[i][j-1], board[i-1][j-1]) + 1
                    if board[i][j] > a:
                        a = board[i][j]


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    print('Hello Python')

    return a**2
