from NFA import NFA
from string import ascii_lowercase
from itertools import product

saved_objects = []

def nfa_input():

    print("Welcome to the NFA prompt")
    while(True):
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
    n = NFA(states,alphabet,lambda x,y:transition_table[x][y],0,finals, epsilon="epsilon")
    print("You have sucessfully created a NFA.")
    return n

while(True):

    print("Welcome to the prompt!")
    print("Choose between : ")
    print("1.input DFA")
    print("2.input NFA")
    print("x. quit")

    tmp = raw_input()
    if(tmp == '1'):
        print("Welcome to the DFA prompt")
        print("Not implemented yet.")
    elif(tmp == '2'):
        saved_objects.append(nfa_input())


    elif(tmp == 'x'):
        print("Good bye.")
        break
    else :
        print("Unrecognized answer.")
        print(tmp)

