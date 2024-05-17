from multiprocessing import Pool
from multiprocessing.pool import AsyncResult
import tictactoe as ttt
from agents.random_agent import random_agent
from agents.human import human
from agents.agent1 import heuristic

def match(agent1, agent2):
    state = ttt.State()

    player = [agent1, agent2]
    turn = 0
    while not state.terminal_test():
        player_move = player[turn](state)
        state = state.result(player_move)
        turn += 1
        turn %=2
    return state.utility()

def tournament(agent1, agent2, rounds: int):
    score = 0

    with Pool() as pool:
        result: list[AsyncResult] = []
        for _ in range(rounds):
            result.append(pool.apply_async(match, args=[agent1, agent2]))
        for res in result:
            score += res.get()
        print(f"score after {rounds} games: {score}\n average {score/float(rounds)}")


def main():
    player = [human, heuristic]
    #player = [heuristic, random_agent]
    #player = [random_agent, heuristic]

    #tournament(player[0], player[1], 100)
    #exit()
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
