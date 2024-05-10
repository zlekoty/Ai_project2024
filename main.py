import tictactoe as ttt
from agents.random_agent import random_agent
from agents.human import human
from agents.agent1 import heuristic

def main():

    #player = [random_agent, random_agent]
    player = [heuristic, human]

    state = ttt.State()

    turn = 0
    while not state.terminal_test():
        player_move = player[turn](state)
        state = state.result(player_move)
        turn += 1
        turn %=2

    print("Final Board:")
    print(state)
    print(f"Result: {state.utility()}")


if __name__ == "__main__":
    main()
