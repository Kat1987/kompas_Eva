def direction(facing, turn):
    facinglist = ['N','NE','E','SE','S','SW','W','NW']
    x = int(turn/45)
    facingindex = facinglist.index(facing)
    y = facingindex + x
    if turn == 0:
        return(facing)
    elif  -8 < y < 8:
        return(facinglist[y])
    else: 
        z = y % 8
        return(facinglist[z])
    
    2 вариант: 
    def direction(facing, turn):
    facinglist = ['N','NE','E','SE','S','SW','W','NW']
    x = int(turn//45)
    facingindex = facinglist.index(facing)
    y = facingindex + x
    return facinglist[y % 8]
