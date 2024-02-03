from tctPiece import tctPiece

# board Object that holds characters for board pieces
board = tctPiece()

class tctBoard:
    def __init__(self):
        # initializes List to hold a 3x3 grid of "empty spaces"
        self.tctList = [[board.empty for _ in range(3)],[board.empty for _ in range(3)],[board.empty for _ in range(3)]]

    # sets List back to "empty"
    def resetBoard(self):
        self.tctList = [[board.empty for _ in range(3)],[board.empty for _ in range(3)],[board.empty for _ in range(3)]]

    # toString to visualize the game board
    def toString(self):
        output = '\n+++Tic Tac Toe Board+++'
        output += '\n        *   *   *    '
        output += '\n3   *   ' + self.tctList[2][0]+'   ' + self.tctList[2][1]+'   ' + self.tctList[2][2] + '   *'
        output += '\n2   *   ' + self.tctList[1][0]+'   ' + self.tctList[1][1]+'   ' + self.tctList[1][2] + '   *'
        output += '\n1   *   ' + self.tctList[0][0]+'   ' + self.tctList[0][1]+'   ' + self.tctList[0][2] + '   *'
        output += '\n        *   *   *    '
        output += '\n        A   B   C    '
        return output

    # @param bool user; checks for player number
    # @param int row,col; holds player's desired row and column
    # method to set a piece onto the board
    def setPiece(self, user, row, col):
        if user:
            self.tctList[row][col] = board.user1
        else:
            self.tctList[row][col] = board.user2

    # @param bool user; checks for player number
    # @param int row,col; holds a row and column to evaluate
    # @return Boolean; to flag if a space is filled
    # checks pieces on board to determine if a spot is filled
    # TODO fix this shit same piece
    def checkPiece(self, row, col,user):
        if user:
            oppositeUser = board.user2
        else:
            oppositeUser = board.user1
        if self.tctList[row][col] == oppositeUser:
            return True
        else:
            return False

    # @param bool user; checks for player number
    # @return int; win/lose/draw or continue condition
    def checkBoard(self,user):
        # assigns every current piece on board a variable to represent it
        a1 = self.tctList[0][0]
        a2 = self.tctList[0][1]
        a3 = self.tctList[0][2]
        b1 = self.tctList[1][0]
        b2 = self.tctList[1][1]
        b3 = self.tctList[1][2]
        c1 = self.tctList[2][0]
        c2 = self.tctList[2][1]
        c3 = self.tctList[2][2]

        # determines if evaluating for player 1
        if user:
            # variable to represent user1's pieces
            piece = board.user1

            # checks if user1 has a valid win condition of 3 in a row, column, or diagonal
            if a1==b1==c1==piece or a2==b2==c2==piece or a3==b3==c3==piece or a1==a2==a3==piece or b1==b2==b3==piece or c1==c2==c3==piece or a1==b2==c3==piece or a3==b2==c1==piece:
                return 1
            else:
                # checks if all pieces have been placed but no victor can be declared
                if all(self.tctList[i][j] != board.empty for i in range(3) for j in range(3)):
                    return 3
                # if no win or draw condition is met, send continue flag
                else:
                    return 0

        # determines if evaluating for player 2
        else:
            # variable to represent user2's pieces
            piece = board.user2

            # checks if user2 has a valid win condition of 3 in a row, column, or diagonal
            if a1==b1==c1==piece or a2==b2==c2==piece or a3==b3==c3==piece or a1==a2==a3==piece or b1==b2==b3==piece or c1==c2==c3==piece or a1==b2==c3==piece or a3==b2==c1==piece:
                return 2
            else:
                # checks if all pieces have been placed but no victor can be declared
                if all(self.tctList[i][j] != board.empty for i in range(3) for j in range(3)):
                    return 3
                else:
                    # if no win or draw condition is met, send continue flag
                    return 0
