def playerOne(u_in):
    bin=0
    if(u_in=='a'):
        bin= 0
    elif(u_in=='b'):
        bin=1
    elif(u_in=='c'):
        bin=2
    elif(u_in=='d'):
        bin=3
    elif(u_in=='e'):
        bin=4
    elif(u_in=='f'):
        bin=5
    elif(u_in=='q'or u_in=='Q'):
        gameOn = False
    else:
        bin=-3
    return bin
        
