from tctBoard import tctBoard

# @param boolean userIn; bool to know if Player 1 or 2
# @return int row, col; desired location of player's piece
def userInput(userIn):

    if userIn:
        userName = "User 1"
    else:
        userName = "User 2"

    #Data validation for player's desired row number
    while True:
        try:
            row = int(input(userName+", enter a row: ")) - 1
            if 0 <= row <= 2:
                break
            else:
                print("Invalid Input, enter a row number")
        except ValueError:
            print("Invalid Input, enter a row number")

    # Data validation for player's desired column using a list
    while True:
        col = input(userName+", enter a column (A-C): ").upper()
        if col in ['A', 'B', 'C']:
            if col == 'A':
                col = 0
            elif col == 'B':
                col = 1
            elif col == 'C':
                col = 2
            break
        else:
            print("Invalid Input, please enter a column letter (A, B, or C)")
    return row, col


# @param boolean turn; determine turn order of players
# @return int; send game ending condition
def ticTacLogic(turn):
    user1 = True
    user2 = False
    ticTacToe = tctBoard()

    # removes any "pieces" currently on board
    ticTacToe.resetBoard()
    # while loop to keep turns alternating
    while True:
        # boolean to check if its player 1 who has first turn
        if turn:
            #
            #   User 1
            #
            # prints current state of the board
            print(ticTacToe.toString())

            # Data Validation to collect user's desired row and col, and ensures space is not taken
            while True:
                row, col = userInput(user1)
                if ticTacToe.checkPiece(row,col,user1):
                    print('This space is preoccupied, try another')
                else:
                    # sets piece on board if desired space is empty
                    ticTacToe.setPiece(user1, row, col)
                    break

            print(ticTacToe.toString())

            # checks if the user's turn either won the game or draw
            if ticTacToe.checkBoard(user1) == 1:
                return 1
            elif ticTacToe.checkBoard(user1) == 3:
                return 0
            #
            #   User 2
            #
            # Data Validation to collect user's desired row and col, and ensures space is not taken
            while True:
                row, col = userInput(user2)
                if ticTacToe.checkPiece(row, col, user2):
                    print('This space is preoccupied, try another')
                else:
                    # sets piece on board if desired space is empty
                    ticTacToe.setPiece(user2, row, col)
                    break

            print(ticTacToe.toString())

            # checks if the user's turn either won the game or draw
            if ticTacToe.checkBoard(user2) == 2:
                return 2
            elif ticTacToe.checkBoard(user2) == 3:
                return 0
        #
        #
        # User 2 First
        # Same as above but reversed
        #
        else:
            #
            #   User 2
            #
            print(ticTacToe.toString())
            while True:
                row, col = userInput(user2)
                if ticTacToe.checkPiece(row, col, user2):
                    print('This space is preoccupied, try another')
                else:
                    ticTacToe.setPiece(user2, row, col)
                    break

            print(ticTacToe.toString())

            if ticTacToe.checkBoard(user2) == 2:
                return 2
            elif ticTacToe.checkBoard(user2) == 3:
                return 0

            #
            #   User 1
            #
            while True:
                row, col = userInput(user1)
                if ticTacToe.checkPiece(row, col, user1):
                    print('This space is preoccupied, try another')
                else:
                    ticTacToe.setPiece(user1, row, col)
                    break

            print(ticTacToe.toString())

            if ticTacToe.checkBoard(user1) == 1:
                return 1
            elif ticTacToe.checkBoard(user1) == 3:
                return 0



def main():
    # running totals for wins, loses, and draws; boolean to set turn order
    user1Wins=0
    user2Wins=0
    draws=0
    turnOrder = True

    # runs ticTacLogic method to find a game end condition
    result = ticTacLogic(turnOrder)

    # while loop to keep game running after first play if desired
    while True:
        # game end condition based responses, and data collection
        if(result==1):
            user1Wins+=1
            print("User 1 has won")
        elif (result==2):
            user2Wins += 1
            print("User 2 has won")
        else:
            draws += 1
            print("Draw")
        # checks if user would like to exit program
        if input('Press N if you would like to exit, or any other key to continue: ').upper()=='N':
            # farwell message into termination
            print('Thank you for playing! '+'User 1 has won '+str(user1Wins)+' times, User 2 has won '+str(user2Wins)+' times')
            break
        # if players continue turn order is swapped
        else:
            if turnOrder:
                turnOrder=False
            else:
                turnOrder=True
            # runs game with updated turnOrder
            result = ticTacLogic(turnOrder)


if __name__ == '__main__':
    main()

