def makeMove(stones, bin_index, isPlayer1,stealing):
    
    x = stones.copy()
    for i in range(0,len(x)):
        x[i]=int(x[i])    
    numStonesInBin= x[bin_index]
    x[bin_index]=0
    valid = True
    playAgain=False
    stealing=stealing
    nextBinToInc=0
    
    ###if hole is empty
    if numStonesInBin==0:
        valid=False
        return x,valid,playAgain
    else:
        valid=True

    if isPlayer1:
        if(stealing):
            for stone in range(0,int(numStonesInBin)):  
                nextBinToInc = bin_index+1+stone    #5+1+8
                if nextBinToInc>=13:
                    nextBinToInc=nextBinToInc%13 #14%13=1
                x[nextBinToInc]= x[nextBinToInc] + 1
            
                #play again if the last stone is in your mancala
                if(int(stone)==int(numStonesInBin)-1 and nextBinToInc==6):
                    playAgain=True
                else:
                    playAgain=False
                #stealing mode
                if(int(stone)==int(numStonesInBin)-1 and x[nextBinToInc]==1):
                    x[6]=x[nextBinToInc]+x[13-nextBinToInc-1]
                    x[nextBinToInc]=0
                    x[13-nextBinToInc-1] =0

            
        else:
            for stone in range(0,int(numStonesInBin)):  
                nextBinToInc = bin_index+1+stone    #5+1+8
                if nextBinToInc>=13:
                    nextBinToInc=nextBinToInc%13 #14%13=1
                x[nextBinToInc]= x[nextBinToInc] +1
            
                #play again if the last stone is in your mancala
                if(int(stone)==int(numStonesInBin)-1 and nextBinToInc==6):
                    playAgain=True
                else:
                    playAgain=False

    #player2
    else:
        if(stealing):
            for stone in range(0,int(numStonesInBin)):  
                nextBinToInc = bin_index+1+stone    #bin_index=12, stone=1+2 
                nextBinToInc= nextBinToInc%14
                if nextBinToInc==6:
                    nextBinToInc=7
                    bin_index+=1           
                x[nextBinToInc]= x[nextBinToInc] +1

                #play again
                if(int(stone)==int(numStonesInBin)-1 and nextBinToInc==13):
                    playAgain=True
                else:
                    playAgain=False
               #stealing mode
                if(int(stone)==int(numStonesInBin)-1 and x[nextBinToInc]==1):
                    x[13]=x[nextBinToInc]+x[13-nextBinToInc-1]                      
                    x[nextBinToInc]=0
                    x[13-nextBinToInc-1]=0
        
        #not stealing for player2 
        else:
          for stone in range(0,int(numStonesInBin)):  
                nextBinToInc = bin_index+1+stone    #bin_index=12, stone=1+2 
                nextBinToInc= nextBinToInc%14
                if nextBinToInc==6:
                    nextBinToInc=7
                    bin_index+=1           
                x[nextBinToInc]= x[nextBinToInc] +1
                #play again
                if(int(stone)==int(numStonesInBin)-1 and nextBinToInc==13):
                    playAgain=True
                else:
                    playAgain=False              
    
    
        for i in range(0,len(x)):
            x[i]=str(x[i])
    return x ,valid,playAgain



