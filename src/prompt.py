from string import ascii_lowercase
from itertools import product

from DFA import DFA
from NFA import NFA
import FiniteStateMachine

saved = {}

def save_prompt(FA):
    """
    Interactive prompt for saving a finite automaton.
    :param FA: A finite automaton
    """
    x = input("If you want to save this finite state machine, please enter a path. \n"+
              "If you do not want to save, press enter.")

    if x == '':
        return
    else :
        FiniteStateMachine.save_machine(FA,x)

def dfa_input():
    """
    Interactive prompt for initializing a DFA
    :return: a DFA
    """
    print("Welcome to the DFA prompt")
    while(True):
        print("Enter a label for your DFA :")
        label = input()

        print("Enter size of alphabet :")
        tmp = input("|E| = ")
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
        tmp = input("|Q| = ")
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
    print(("States : ",states))
    print(("Alphabet : ", alphabet))

    #Final states in input
    while(True):
        print("Enter final states (ex. \"0,3,5\") :")
        tmp = input("F = ")
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
                    tmp = input(str(s)+" -"+str(a)+"-> ")
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
    :return: a NFA
    """

    print("Welcome to the NFA prompt")
    while(True):
        print("Enter a label for your NFA :")
        label = input()
    
        print("Enter size of alphabet :")
        tmp = input("|E| = ")
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
        tmp = input("|Q| = ")
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
    print(("States : ",states))
    print(("Alphabet : ", alphabet))

    #Final states in input
    while(True):
        print("Enter final states (ex. \"0,3,5\") :")
        tmp = input("F = ")
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
                    tmp = input(str(s)+" -"+str(a)+"-> ")
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

        tmp = input()
        if(tmp == '1'):
            dfa = dfa_input()
            saved[dfa.label] = dfa
            save_prompt(dfa)
        elif(tmp == '2'):

            nfa = nfa_input()
            saved[nfa.label] = nfa
            save_prompt(nfa)
        elif(tmp == 'x'):
            break
        else :
            print("Unrecognized answer.")
            print(tmp)

    print("See dictionnary \"saved\" for created state machines.")
