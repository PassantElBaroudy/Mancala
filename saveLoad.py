def saveLoad(stonesAmount,gameMode,Stealing,gameDepth,Save,Load):
    if Save:
        textfile = open("savedGame.txt", "w")
        textfile.write(gameMode+ "\n")
        if Stealing:
            textfile.write('1'+ "\n")
        else:
            textfile.write('0'+ "\n")
        textfile.write(str(gameDepth)+ "\n")
        for element in stonesAmount:
            textfile.write(element.strip() + "\n")
        textfile.close() 
        print("Game Saved in savedGame.txt")
    elif Load:
        file1 = open('savedGame.txt', 'r')
        Lines = file1.readlines()
        gameMode = Lines[0].strip()
        if (Lines[1].strip() == '1'):
            Stealing = True
        else:
            Stealing = False
        gameDepth = Lines[2].strip()
        for i in range(14):
            stonesAmount[i] = Lines[i+3].strip()
        return stonesAmount,gameMode,Stealing,gameDepth