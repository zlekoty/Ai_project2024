import math
import random
import tictactoe as ttt

def heuristic(s: ttt.State) -> ttt.Action:
    """
        Returns an action found using heuristic search with alpha beta pruning.
    """

    max_depth = 2
    #do we have to evaluate potential states (after performing actions) and choose the best???
    
    def feature1(s):
        #ex check if possible to have 3 in row  
        pass

    def feature2(s):
        #ex check if opponent can have 3 in row
        pass

    #..........

    def evaluation(s: ttt.State, player) -> float:
        if s.terminal_test():
            return s.utility(player)
        
        r = random.random()

        return r

    
    def heuristic_alpha_beta_search(state: ttt.State) -> ttt.Action:
        player = state.player()
        value, move = max_value(state, player, -math.inf, math.inf, 0)
        return move
    
    def max_value(state: ttt.State, player, alpha, beta, depth: int) -> tuple[float, ttt.State | None]:
        if is_cutoff(state, depth):
            return (evaluation(state, player), None)
        v:float = -math.inf
        
        for action in state.actions():
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
        for action in state.actions():
            v2, _ = max_value(state, state.result(action), alpha, beta, depth + 1)
            if v2 < v:
                v, move = v2, action
                beta = min(beta, v)
            if v <= alpha:
                return v, move
        return v, move
    
    def is_cutoff(state, depth) -> bool:
        return depth >= max_depth or state.terminal_test()
    
    return heuristic_alpha_beta_search(s)
