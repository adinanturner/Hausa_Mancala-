class MancalaBoard:
    def __init__(self):
        # The keys are the indices of the 12 pits and 2 stores, and the values are the number of seeds inside them.
        self.board = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4,
                      "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,
                      1: 0, 2: 0}
        # the letters of Player 1's pits:
        self.fosses1 = ("A", "B", "C", "D", "E", "F")
        #the letters of Player 2's pit 2:
        self.fosses2 = ("G", "H", "I", "J", "K", "L")
        # The opposite pit
        self.opposite = {"A": "G", "B": "H", "C": "I", "D": "J", "E": "K",
                         "F": "L", "G": "A", "H": "B", "I": "C", "J": "D", "K": "E", "L": "F"}
        # The next pit
        self.next = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": 1,
                     1: "L", "L": "K", "K": "J", "J": "I", "I": "H", "H": "G", "G": 2, 2: "A"}

    def possibleMoves(self, player):
        # This function will return the pits of the player that still contain seeds
        PossibleMoves = []
        if (player == 1):
            for fosse in self.fosses1:
                if (self.board[fosse] != 0):
                    PossibleMoves.append(fosse)
        else:
            for fosse in self.fosses2:
                if (self.board[fosse] != 0):
                    PossibleMoves.append(fosse)
        return PossibleMoves

    def doMove(self, player, position):
        # This function executes a move and returns the number of the player who will play next.
        # It picks a pit on their side of the board and collects all the seeds from it.

        graines = self.board[position]
        self.board[position] = 0
        # Moving counterclockwise, the player drops one seed in each pit
        # until they have no more seeds left in their hand.

        while graines > 0:
            position = self.next[position]
            self.board[position] += 1
            graines = graines-1
        # If the last seed lands in the player's store, that player gets an extra turn.
        if (position == player):
            return player
        # If the last seed lands in an empty pit on the player's side,
        # that seed and all the seeds in the directly opposite pit (on the opponent's side)
        # are captured by the player and placed in their store.

        if (player == 1):
            player_fosses = self.fosses1
        else:
            player_fosses = self.fosses2
        if (self.board[position] == 1 and position in player_fosses):
            self.board[position] = 0
            oppositePosition = self.opposite[position]
            self.board[player] += (self.board[oppositePosition]+1)
            self.board[oppositePosition] = 0

        if (player == 1):
            return 2
        else:
            return 1
