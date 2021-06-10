def winner(board):
    for i in range(0,len(board)):
        board[i]=int(board[i])     
    w=0
    winner=''
    player1Holes=board[0:6]
    player2Holes=board[7:13]

    if(sum(player1Holes)==0):
        board[13]+=sum(player2Holes)
        for hole in range(7,13):
            board[hole]=0
        w=1
    elif(sum(player2Holes)==0):
        board[6]+=sum(player1Holes)
        for hole in range(0,6):
            board[hole]=0
        w=1

    if w==1:
        if board[6]>board[13]:
            winner = "wohoooo!!! player1 wins with score "+str(board[6])
            print(winner)
        elif board[13]>board[6]:        
            winner = "wohoooo!!! player2 wins with score "+str(board[13])
            print(winner)
        return board,winner,w
    return board,winner,w