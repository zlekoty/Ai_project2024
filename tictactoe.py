import numpy as np

def board_map(board): #used in board visualisation
        symbol_map = {0: " ", 1: "o", 2: "x"}
        return [symbol_map[value] for value in board]

class Action:
    def __init__(self, board:int, cell: int):
        self.board = board
        self.cell = cell

class State:
    board = np.zeros((9, 9))
    player = 2

    def player(self):
        """
        Returns which player's turn it is
        """
        pass

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
        new_State = State()
        board = a.board
        cell = a.cell
        player = self.player
        new_State.board[int(board)][int(cell)] = float(player)
        return new_State

    def utility(self):
        """
        Returns the utility of this State
        """
        if not self.terminal_test():
            return None
        
        #return 1 
            
        pass

    def terminal_test(self) -> bool:
        """
        Returns whether this is a terminal state
        """

        # are there any empty spots left?

        # is there a winner?

        pass

    def __str__(self):
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
def agent(s):
    possible_actions = s.actions()
    return possible_moves[0]


def main():
    s = State()

    for x in s.actions():
        b = s.result(x)
        print(b)

if __name__ == "__main__":
    main()