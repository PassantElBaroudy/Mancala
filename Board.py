#gameOn = True
#firstPlayer = True

# stonesAmount = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
#stonesAmount=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] 
def Board(stonesAmount,first):
    for i in range(len(stonesAmount)):
        if int(stonesAmount[i]) < 10:
            stonesAmount[i] = str(stonesAmount[i]).replace(" ","")
            stonesAmount[i] = " "+str(stonesAmount[i])
        else:
            stonesAmount[i] = str(stonesAmount[i])
    

            
    if (first): 
        print(" ")       
        print("+----+----+----+----+----+----+----+----+")
        print("|    | "+stonesAmount[12]+" | "+stonesAmount[11]+" | "+stonesAmount[10]+" | "+stonesAmount[9]+" | "+stonesAmount[8]+" | "+stonesAmount[7]+" |    |")
        print("| "+stonesAmount[13]+" +----+----+----+----+----+----+ "+stonesAmount[6]+" |")
        print("|    | "+stonesAmount[0]+" | "+stonesAmount[1]+" | "+stonesAmount[2]+" | "+stonesAmount[3]+" | "+stonesAmount[4]+" | "+stonesAmount[5]+" |    |")
        print("+----+----+----+----+----+----+----+----+")
        print("       a    b    c    d    e    f")
        print(" ")
        print("                YOUR TURN         ")
        print("------------------------------------------")
        print(" ")       

        
    else:
        print(" ")
        print("------------------------------------------")
        print("                YOUR TURN         ")
        print(" ")
        print("       f    e    d    c    b    a")
        print("+----+----+----+----+----+----+----+----+")
        print("|    | "+stonesAmount[12]+" | "+stonesAmount[11]+" | "+stonesAmount[10]+" | "+stonesAmount[9]+" | "+stonesAmount[8]+" | "+stonesAmount[7]+" |    |")
        print("| "+stonesAmount[13]+" +----+----+----+----+----+----+ "+stonesAmount[6]+" |")
        print("|    | "+stonesAmount[0]+" | "+stonesAmount[1]+" | "+stonesAmount[2]+" | "+stonesAmount[3]+" | "+stonesAmount[4]+" | "+stonesAmount[5]+" |    |")
        print("+----+----+----+----+----+----+----+----+")
        print(" ")
        print("------------------------------------------")


