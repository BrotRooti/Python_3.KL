'''
Tic Tac Toe
Phillip
Game-code 14.03.22
'''

x_dim = 3
y_dim = 3

def display(liste):
    #eigener loop für die koordinaten anzeige
    for x in range(x_dim):
        print(" {}".format(x),end='')
    print()
    
    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(liste[x][y]),end ='')
        print("| {}".format(y))

def check_for_win():
    #if a player has 3 in a row or diagonal then return 1
    #else return 0
    for row in range(0,3,1):
        if(playing_field[0][row] == playing_field[1][row] == playing_field[2][row] != " "):
            return 1
        elif(playing_field[row][0] == playing_field[row][1] == playing_field[row][2] != " "):
            return 1
    if(playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != " "):
        return 1
    elif(playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != " "):
        return 1
    return 0
    

#### Main programm starts here ####
playing_field = [[" " for i in range(y_dim)] for j in range (x_dim)]


display(playing_field)

#variables wich we will need 
counter = 0
player = 1
symbol = 'X'

#main game loop starts here
while True:
    x_cord = int(input("PLayer {} enter x-coordinate ->".format(player)))
    y_cord = int(input("PLayer {} enter y-coordinate ->".format(player)))
    if (x_cord >= x_dim or y_cord >= y_dim or x_cord < 0 or y_cord < 0):
        print("You stupid ;) \nJust joking your coordinates are out of range, please try again!")
        continue
        
    else:
        #coordinates are on the playing_field
        #check if this field is still free?
        if (playing_field[x_cord][y_cord] == ' '):
            #field is free
            playing_field[x_cord][y_cord] = symbol
        else:
            print("This field is already taken!")
            continue
        
        #display the playing_field
        display(playing_field)
        
        #update counter
        counter = counter + 1
        
        #check for draw
        if (counter == 9):
            print("The game is a DRAW!")
            break

        #check for win
        if (check_for_win()):
            print("Congratulations Player {} you won !!!".format(player))
            break
        
        
        #change player
        if (player == 1):
            player = 2
            symbol = 'O'
        else:
            player = 1
            symbol = 'X'
