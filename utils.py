import pickle
#Some small utils

def get_transition_table(func, states, alphabet):
    """
    Build a transition table for func, a function such [states] X [alphabet] -> [states]
    Returns a dictionnary of states where each element is a dictionnary with (key,value) = [alphabet],[states]
    """
    d = {}
    for x in sorted(states):
        d[x] = {}
        for c in alphabet:
            d[x][c] = func(x,c)
#        d[x].update(map(lambda c: (c,func(x, c)), alphabet.copy()))    
    return d
    
def save_machine(FA,path):
    "Saves a single automaton"

    FA = FA.copy()

    # Pickle cannot serialize lambda functions. We will instead serialize a transition table of the function.
    FA.delta = get_transition_table(FA.delta,FA.states,FA.alphabet)

    f = open(path,'wb')
    p = pickle.Pickler(f,2)
    p.dump(FA)
    print("Saved object at "+f.name)
    


def load_machine(path):
    """ Loads a single automaton """
    FA = pickle.load(open(path,'r'))

    # Make the transition table a lambda function.
    FA.delta = lambda x,c : FA.delta[x][c]
    return FA
