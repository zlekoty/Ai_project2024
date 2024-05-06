import tictactoe as ttt

def human(s: ttt.State):
    def prompt():
        print(s)
        print(f"Player {s.player()} to move")
        move = input('Enter move (e.g 0,4): ')
        board, cell = (int(x) for x in move.split(','))
    
        return ttt.Action(board, cell)

    a = prompt()

    while a not in s.actions():
        print("INVALID MOVE!, try again")
        a = prompt()

    return a
