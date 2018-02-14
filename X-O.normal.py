
#function to print the matrix

def show_state(state):
    print(state[0],state[1],state[2])
    print(state[3],state[4],state[5])
    print(state[6],state[7],state[8])

# Start with player 1

player = 1


#function of Possible win moves

def win_state(state,player):
    if state[0]==('X') and state[1]==('X') and state[2]==('X') or  state[0]==('O') and state[1]==('O') and state[2]==('O') :
        return("Win")
    if state[3]==('X') and state[4]==('X') and state[5]==('X') or  state[3]==('O') and state[4]==('O') and state[5]==('O') :
        return("Win")
    if state[6]==('X') and state[7]==('X') and state[8]==('X') or  state[6]==('O') and state[7]==('O') and state[8]==('O')  :
        return("Win")
    if state[0]==('X') and state[3]==('X') and state[6]==('X') or  state[0]==('O') and state[3]==('O') and state[6]==('O') :
        return("Win")
    if state[1]==('X') and state[4]==('X') and state[7]==('X') or  state[1]==('O') and state[4]==('O') and state[7]==('O') :
        return("Win")
    if state[2]==('X') and state[5]==('X') and state[8]==('X') or  state[2]==('O') and state[5]==('O') and state[8]==('O') :
        return("Win")
    if state[0]==('X') and state[4]==('X') and state[8]==('X') or  state[0]==('O') and state[4]==('O') and state[8]==('O') :
        return("Win")
    if state[2]==('X') and state[4]==('X') and state[6]==('X') or  state[2]==('O') and state[4]==('O') and state[6]==('O') :
        return("Win")
    for position in range(9):
        if state[position]==0:
            return
    return("Stalement")    
    
# Starting initializing the game

state = [0,0,0,0,0,0,0,0,0] 







show_state(state)

while True:

    # print player state
    print("player",player,"move:")
    # inbut the move
    move=int(input("What is your move:"))

    # prevent playing on the same location
    valid_moves=[]
    for position in range(9):
        if state[position]==0:
            valid_moves.append(position)
        if move in valid_moves:
            break
            print("Illegale Move!!")

        

    # making player1 = x and player2 = O
    state[move]=player
    if state[move]==1:
        state[move]='X'
    elif state[move]==2:
        state[move]='O'
    

        
    # update the matrix
    show_state(state)
        



    # Decide who is the winner
    status=win_state(state,player)
 

    if status=="Win":
        print("player",player,"wins")
        break
    
    if status=="Lose":
        print("player",player,"Lose")
        break
    
    if status=="Stalement":
        print("player",player,"Stalement")
        break

    
    if player==1:
        player=2
    else:
        player=1

        

# End the game        

    
print("game is over!.")



   
        


    

    









    





    
