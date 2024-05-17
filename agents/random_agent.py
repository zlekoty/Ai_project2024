import random

def random_agent(s):
    """
        Agent that performs random moves
    """
    possible_actions = s.actions()
    assert(len(possible_actions) > 0)
    
    return random.choice(possible_actions)
