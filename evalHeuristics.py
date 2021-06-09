def evalHeuristics(stonesEval):
    player1Stones = 0
    player2Stones = 0
    
    for i in range(14):
        if i < 7:
            player1Stones += int(stonesEval[i])
        else:
            player2Stones += int(stonesEval[i])
            
    return player1Stones - player2Stones


