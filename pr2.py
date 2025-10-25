
def sq_rt():
    squares = []
    for i in range(1,20+1): #Giving range
        if i%2 != 0: #condition to check odd
            sq = (i ** 2) 
            squares.append(sq)        
    print("The squares of odd values:",squares)
            
sq_rt()        