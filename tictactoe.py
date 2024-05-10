import numpy as np


def board_map(board): #used in board visualisation
        symbol_map = {0: " ", 1: "x", 2: "o"}
        return [symbol_map[value] for value in board]


class Action:
    def __init__(self, board:int, cell: int):
        self.board = board
        self.cell = cell

    def __repr__(self):
        return f'Board: {self.board}, cell: {self.cell}'

    def __eq__(self, other):
        return (self.board == other.board) and (self.cell == other.cell)
        
        

class State:
    board = np.zeros((9, 9), dtype=int)
    turn_player = 1

    def player(self) -> int:
        """
        Returns which player's turn it is
        """
        return self.turn_player


    def actions(self) -> list[Action]:
        """
        Returns the possible actions from this game state
        """
        
        actions = []

        for b in range(len(self.board)):
            for cell in range(len(self.board[0])):
                if self.board[b][cell] == 0:
                    actions.append(Action(b, cell))

        return actions

    
    def result(self, a: Action):
        """
        Returns the State resulting from applying the action
        """
        assert(not a is None)
        action_board = a.board
        action_cell = a.cell
        
        if self.board[action_board][action_cell] != 0:
            raise ValueError('Illegal action. Only actions on empty cells are allowed.')

        new_state = State()
        player = self.player()
        
        new_state.board = self.board.copy()
        new_state.board[action_board][action_cell] = player

        if player == 1:
            new_state.turn_player = 2
        else:
            new_state.turn_player = 1

        return new_state


    def utility(self, player:int=1) -> None | float:
        """
        Returns the utility of this State
        """
        if not self.terminal_test():
            return None

        def f():
                        
            winner = self.winner()
            if winner is None:
                #draw
                return 1/2
            if winner == 1:
                #x
                return 1
            else:
                #o
                return 0
        if player == 1:
            return f()
        else:
            return 1 - f()


    def terminal_test(self) -> bool:
        """
        Returns whether this is a terminal state
        """

        if 0 not in self.board.flatten():
            #no empty spots left
            return True

        if self.winner() is not None:
            return True
        
        return False


    def winner(self) -> None | int:
        
        def winner_of_board(b: np.ndarray) -> None | int:
            for player in [1,2]:
                if ((b[0]==b[1]==b[2]==player) or (b[3]==b[4]==b[5]==player) or (b[6]==b[7]==b[8]==player) or
                    (b[0]==b[3]==b[6]==player) or (b[1]==b[4]==b[7]==player) or (b[2]==b[5]==b[8]==player) or 
                    (b[0]==b[4]==b[8]==player) or (b[2]==b[4]==b[6]==player)):
                    return player
            return None

        big_board = np.zeros(9, dtype=int)

        for (index, small_board) in enumerate(self.board):
            winner = winner_of_board(small_board)
            if winner is None:
                big_board[index] = 0
            else:
                big_board[index] = winner

        return winner_of_board(big_board)


    def __repr__(self):
        return """
                {a[0]}{a[1]}{a[2]}|{b[0]}{b[1]}{b[2]}|{c[0]}{c[1]}{c[2]}
                {a[3]}{a[4]}{a[5]}|{b[3]}{b[4]}{b[5]}|{c[3]}{c[4]}{c[5]}
                {a[6]}{a[7]}{a[8]}|{b[6]}{b[7]}{b[8]}|{c[6]}{c[7]}{c[8]}
                ------------
                {d[0]}{d[1]}{d[2]}|{e[0]}{e[1]}{e[2]}|{f[0]}{f[1]}{f[2]}
                {d[3]}{d[4]}{d[5]}|{e[3]}{e[4]}{e[5]}|{f[3]}{f[4]}{f[5]}
                {d[6]}{d[7]}{d[8]}|{e[6]}{e[7]}{e[8]}|{f[6]}{f[7]}{f[8]}
                ------------
                {g[0]}{g[1]}{g[2]}|{h[0]}{h[1]}{h[2]}|{i[0]}{i[1]}{i[2]}
                {g[3]}{g[4]}{g[5]}|{h[3]}{h[4]}{h[5]}|{i[3]}{i[4]}{i[5]}
                {g[6]}{g[7]}{g[8]}|{h[6]}{h[7]}{h[8]}|{i[6]}{i[7]}{i[8]}

                """.format(a=board_map(self.board[0]), b=board_map(self.board[1]), c=board_map(self.board[2]), 
                            d=board_map(self.board[3]),e=board_map(self.board[4]), f=board_map(self.board[5]), 
                            g=board_map(self.board[6]), h=board_map(self.board[7]), i=board_map(self.board[8]))

