import math
import random
import os
import tictactoe as ttt
import numpy as np

def heuristic(s: ttt.State) -> ttt.Action:
    """
        Returns an action found using heuristic search with alpha beta pruning.
    """

    max_depth = int(os.getenv('DEPTH', 2))
    #do we have to evaluate potential states (after performing actions) and choose the best???
    
    def feature1(s):
        #ex check if possible to have 3 in row  
        pass

    def feature2(s):
        #ex check if opponent can have 3 in row
        pass

    def feature_n_in_a_row(s: ttt.State, player:int, n: int):
        """
        """
        #0,1,2,...,8
        big_board = s.big_board()
        def evaluate_file(x,y,z, player, n):
            a = [x,y,z]
            if player == 1:
                opponent = 2
            else:
                opponent = 1
            count = a.count(player) == n
            count_opponent = a.count(opponent) 
            if(count == n and count_opponent == 0):
                return 1
            else:
                return 0
        matches = 0
        ls = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,8)]
        for (x,y,z) in ls:
            matches = matches + evaluate_file(big_board[x],big_board[y],big_board[z], player, n)
        return matches

    def feature_won_subgames(s: ttt.State, player: int):
        count = 0
        for board in range(9):
            if s.winner_of_board_index(board) == player:
                count = count + 1
        return float(count) / 9

    

    #..........

    def evaluation(s: ttt.State, player) -> float:
        if s.terminal_test():
            print(f"evaluation: return utility: {s.utility(player)}, from POV of player {player}")
            return s.utility(player)
        
        
        if player == 1:
            opponent = 2
        else:
            opponent = 1
        #normalize
        eval = 3*feature_n_in_a_row(s, player, 2) + feature_n_in_a_row(s, player, 1)\
              - (3*feature_n_in_a_row(s, opponent, 2) + feature_n_in_a_row(s, opponent, 1) )
        #print(f"evaluation: return evaluation: {eval}, from POV player {player}")
        return eval
        #return random.random()
    
    def heuristic_alpha_beta_search(state: ttt.State) -> ttt.Action:
        player = state.player()
        _, move = max_value(state, player, -math.inf, math.inf, 0)
        return move
    
    def max_value(state: ttt.State, player, alpha, beta, depth: int) -> tuple[float, ttt.State | None]:
        if is_cutoff(state, depth):
            return (evaluation(state, player), None)
        v:float = -math.inf
        
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            v2, _ = min_value(state.result(action), player, alpha, beta, depth + 1)
            if v2 > v:
                v, move = v2,action
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
        return v, move
        

    def min_value(state: ttt.State, player, alpha, beta, depth: int) -> tuple[float, ttt.State | None]:
        if is_cutoff(state, depth):
            return (evaluation(state, player), None)
        v = math.inf
        
        actions = state.actions()
        random.shuffle(actions)
        for action in actions:
            v2, _ = max_value(state.result(action), player, alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, action
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move
    
    def is_cutoff(state, depth) -> bool:
        return depth >= max_depth or state.terminal_test()
    
    return heuristic_alpha_beta_search(s)
