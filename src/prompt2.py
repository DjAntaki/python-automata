from string import ascii_lowercase
from itertools import product

from DFA import DFA
import FiniteStateMachine
from NFA import NFA

"""
This modules contains some functions to interactively create NFA and DFA.
If run this file using the command "python3 -i prompt.py" (or "python -i prompt2.py" if you uses an earlier version of python),
you can create your NFAs and DFAs, quit the main loop and then use the python interpreter to play with your automata.

The created automata are stored in the dictonnary variable 'automata' and can be accessed
in the python interpreter using the precedently given label.


Here is an example of typical use :

| .../python_automata/src$ python3 -i prompt.py
Welcome to the make-your-own-automata prompt interface!
This script needs to be run with the -i command.
Choose between :
1.create DFA
2.create NFA
x. Go to python prompt and access created automata
1
Welcome to the DFA prompt
Enter a label for your DFA :
dfa1
Enter size of alphabet :
|E| = 2
Enter size of the set of states :
|Q| = 2
('States : ', set([0, 1]))
('Alphabet : ', set(['a', 'b']))
Enter final states (ex. "0,3,5") :
F = 1
You will now enter the following states for each transitions. (ex. "0,3,5")
If you do not wish for a transition to exist, press enter
0 -a-> 0
0 -b-> 1
1 -a->
1 -b-> 1
You have sucessfully created a DFA.
If you want to save this finite state machine, please enter a path.
If you do not want to save, press enter. automatas/dfa1.aut



| >>>
| >>>
|     ...
| >>>
| >>>




"""

automata = {}

def save_prompt(FA):
    """
    Interactive prompt for saving a finite automaton. Creates a file at entered path.
    :param FA: A finite automaton
    """
    x = raw_input("If you want to save this finite state machine, please enter a path. \n"+
              "If you do not want to save, press enter.")

    if x == '':
        return
    else :
        FiniteStateMachine.save_machine(FA,x)

def dfa_input():
    """
    Interactive prompt for initializing a DFA
    :return: the DFA created
    """
    print("Welcome to the DFA prompt")
    while(True):
        print("Enter a label for your DFA :")
        label = raw_input()

        print("Enter size of alphabet :")
        tmp = raw_input("|E| = ")
        try:
            e_size = int(tmp)
            assert e_size>0
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Building the alphabet
    alphabet = set()
    e,x = 0,1
    while(True):
        for i in product(ascii_lowercase, repeat=x):
            alphabet.add(''.join(i))
            e += 1
            if(e == e_size):
                break

        if(e == e_size):
            break
        else :
            x += 1


    #Input
    while(True):
        print("Enter size of the set of states :")
        tmp = raw_input("|Q| = ")
        try:
            q_size = int(tmp)
            assert q_size >0
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Building the states
    states = set(range(q_size))

    #Printing some info
    print("States : ",states)
    print("Alphabet : ", alphabet)

    #Final states in input
    while(True):
        print("Enter final states (ex. \"0,3,5\") :")
        tmp = raw_input("F = ")
        try:
            finals = [int(i) for i in tmp.replace(" ", '').split(',')]
            assert all([i in states for i in finals])
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Taking each transition
    print("You will now enter the following states for each transitions. (ex. \"0,3,5\")")
    print("If you do not wish for a transition to exist, press enter")
    transition_table = [{x:None for x in alphabet} for i in range(q_size)]

    for s in states :
        for a in alphabet :

            while(True):
                try :
                    tmp = raw_input(str(s)+" -"+str(a)+"-> ")
                    if tmp == '':
                        transition_table[s][a] = None
                        break
                    tmp = tmp.replace(" ", '').split(',')
                    tmp = [int(i) for i in tmp]
                    assert all([i in states for i in tmp])
                    transition_table[s][a] = set(tmp)

                except Exception :
                    print("Incorrect input.")
                    continue
                break

#   def __init__(self, states, alphabet, delta, start, accepts, epsilon='epi'):
    n = DFA(states,alphabet,lambda x,y:transition_table[x][y],0,finals)
    n.label = label
    print("You have sucessfully created a DFA.")

    return n

def nfa_input():
    """
    Interactive prompt for initializing a NFA.
    :return: the created NFA
    """

    print("Welcome to the NFA prompt")
    while(True):
        print("Enter a label for your NFA :")
        label = raw_input()
    
        print("Enter size of alphabet :")
        tmp = raw_input("|E| = ")
        try:
            e_size = int(tmp)
            assert e_size>0
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Building the alphabet
    alphabet = set()
    e,x = 0,1
    while(True):
        for i in product(ascii_lowercase, repeat=x):
            alphabet.add(''.join(i))
            e += 1
            if(e == e_size):
                break

        if(e == e_size):
            break
        else :
            x += 1


    #Input
    while(True):
        print("Enter size of the set of states :")
        tmp = raw_input("|Q| = ")
        try:
            q_size = int(tmp)
            assert q_size >0
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Building the states
    states = set(range(q_size))

    #Printing some info
    print("States : ",states)
    print("Alphabet : ", alphabet)

    #Final states in input
    while(True):
        print("Enter final states (ex. \"0,3,5\") :")
        tmp = raw_input("F = ")
        try:
            finals = [int(i) for i in tmp.replace(" ", '').split(',')]
            assert all([i in states for i in finals])
        except Exception:
            print("Incorrect input.")
            continue
        break

    #Taking each transition
    print("You will now enter the following states for each transitions. (ex. \"0,3,5\")")
    print("If you do not wish for a transition to exist, press enter")
    alphabet.add('epsilon')
    transition_table = [{x:None for x in alphabet} for i in range(q_size)]

    for s in states :
        for a in alphabet :

            while(True):
                try :
                    tmp = raw_input(str(s)+" -"+str(a)+"-> ")
                    if tmp == '':
                        transition_table[s][a] = None
                        break
                    tmp = tmp.replace(" ", '').split(',')
                    tmp = [int(i) for i in tmp]
                    assert all([i in states for i in tmp])
                    transition_table[s][a] = set(tmp)

                except Exception :
                    print("Incorrect input.")
                    continue
                break

#   def __init__(self, states, alphabet, delta, start, accepts, epsilon='epi'):
    alphabet.remove('epsilon')
    n = NFA(states,alphabet,lambda x,y:transition_table[x][y],0,finals, epsilon="epsilon")
    n.label = label
    print("You have sucessfully created a NFA.")

    return n

if __name__ == '__main__':
    print("This script needs to be run with the -i command.")

    while(True):

        print("Welcome to the make-your-own-automata prompt interface!")
        print("Choose between : ")
        print("1.create DFA")
        print("2.create NFA")
        print("x. Go to python prompt and access created automata")

        tmp = raw_input()
        if(tmp == '1'):
            dfa = dfa_input()
            automata[dfa.label] = dfa
            save_prompt(dfa)
        elif(tmp == '2'):

            nfa = nfa_input()
            automata[nfa.label] = nfa
            save_prompt(nfa)
        elif(tmp == 'x'):
            break
        else :
            print("Unrecognized answer.")
            print(tmp)

    print("See dictionnary \"automata\" for created state machines.")
