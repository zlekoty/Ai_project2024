from multiprocessing import Pool
from multiprocessing.pool import AsyncResult

import tictactoe as ttt
from agents.random_agent import random_agent
from agents.human import human
from agents.heuristic_1 import heuristic as heuristic_1
from agents.heuristic_2 import heuristic as heuristic_2
from agents.heuristic_random import heuristic as heuristic_random

def match(agent1, agent2):
    state = ttt.State()

    player = [agent1, agent2]
    turn = 0
    while not state.terminal_test():
        player_move = player[turn](state)
        state = state.result(player_move)
        turn += 1
        turn %=2
    return state.utility(), state.winner()

def tournament(agent1, agent2, rounds: int):
    #score = 0
    won_games = [0, 0]

    with Pool() as pool:
        result: list[AsyncResult] = []
        for _ in range(rounds):
            result.append(pool.apply_async(match, args=[agent1, agent2]))
        for res in result:
            utility, winner = res.get()

            if winner is not None:
                won_games[winner-1] += 1

        print(f"score after {rounds} games: {won_games}, draws: {rounds - (won_games[0] + won_games[1])}")
        print(f"percentages: player X {won_games[0] / rounds}")
        print(f"percentages: player O {won_games[1] / rounds}")


def main():
    player = [heuristic_2, human]
    #player = [heuristic_1, random_agent]
    
    print(f"tournament: {player[0]} vs {player[1]}")
    #tournament(player[0], player[1], int(1e1))

    #print(f"tournament: {player[1]} vs {player[0]}")
    #tournament(player[1], player[0], int(1e2))
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
