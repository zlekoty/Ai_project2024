import random

def random_agent(s):
    """
        Agent that performs random moves
    """
    possible_actions = s.actions()
    
    return random.choice(possible_actions)
