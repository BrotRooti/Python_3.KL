'''
Tic Tac Toe
Phillip
Game-code 14.03.22
'''

import mysql.connector as mariadb

mydb = None
mycursor = None

x_dim = 3
y_dim = 3


def database_setup():
    global mydb
    mydb = mariadb.connect(host="localhost", user="phil", password="phil")
    global mycursor
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS TicTacToe;")
    mycursor.execute("USE TicTacToe;")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS game (player_name VARCHAR(20) PRIMARY KEY, wins INT, draws INT,losses INT);")


def end_game(player1, player2, draw, winner=None):
    mycursor.execute("INSERT IGNORE INTO game (player_name,wins,draws,losses) VALUES (%s,0,0,0);", (player1,))
    mycursor.execute("INSERT IGNORE INTO game (player_name,wins,draws,losses) VALUES (%s,0,0,0);", (player2,))

    if draw:
        mycursor.execute("UPDATE game SET draws = draws + 1 WHERE player_name = %s;", (player1,))
        mycursor.execute("UPDATE game SET draws = draws + 1 WHERE player_name = %s;", (player2,))
    else:
        mycursor.execute("UPDATE game SET wins = wins + 1 WHERE player_name = %s;", (winner,))
        if winner == player1:
            mycursor.execute("UPDATE game SET losses = losses + 1 WHERE player_name = %s;", (player2,))
        else:
            mycursor.execute("UPDATE game SET losses = losses + 1 WHERE player_name = %s;", (player1,))
    mydb.commit()

    exit()


def display(liste):
    # eigener loop für die koordinaten anzeige
    for x in range(x_dim):
        print(" {}".format(x), end='')
    print()

    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(liste[x][y]), end='')
        print("| {}".format(y))


def check_for_win():
    # if a player has 3 in a row or diagonal then return 1
    # else return 0
    for row in range(0, 3, 1):
        if (playing_field[0][row] == playing_field[1][row] == playing_field[2][row] != " "):
            return 1
        elif (playing_field[row][0] == playing_field[row][1] == playing_field[row][2] != " "):
            return 1
    if (playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != " "):
        return 1
    elif (playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != " "):
        return 1
    return 0


#### Main programm starts here ####
playing_field = [[" " for i in range(y_dim)] for j in range(x_dim)]

database_setup()

print("Welcome to Tic Tac Toe!")
print("Player 1, what is your name?")
player1 = input()
print("Player 2, what is your name?")
player2 = input()

print(f"{player1} is using X and {player2} is using 0")

display(playing_field)

# variables wich we will need
counter = 0
player = player1
symbol = 'X'

# main game loop starts here
while True:
    x_cord = int(input("{} enter your x-coordinate ->".format(player)))
    y_cord = int(input("{} enter your y-coordinate ->".format(player)))
    if (x_cord >= x_dim or y_cord >= y_dim or x_cord < 0 or y_cord < 0):
        print("You stupid ;) \nJust joking your coordinates are out of range, please try again!")
        continue

    else:
        # coordinates are on the playing_field
        # check if this field is still free?
        if (playing_field[x_cord][y_cord] == ' '):
            # field is free
            playing_field[x_cord][y_cord] = symbol
        else:
            print("This field is already taken!")
            continue

        # display the playing_field
        display(playing_field)

        # update counter
        counter = counter + 1

        # check for draw
        if (counter == 9):
            print("The game is a DRAW!")
            end_game(player1, player2, True)

        # check for win
        if (check_for_win()):
            print("Congratulations {} you won !!!".format(player))
            end_game(player1, player2, False, player)

        # change player
        if (player == player1):
            player = player2
            symbol = 'O'
        else:
            player = player1
            symbol = 'X'
