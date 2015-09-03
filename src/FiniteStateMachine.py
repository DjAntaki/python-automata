#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
from itertools import product
# Some small utils

class FiniteStateMachine:
    """
    An abstract class that is both inherited by deterministic automata (DFA) and non-deterministic automata (NFA).
    """

    def getAlphabet(self):
        """
        Returns a set containing the alphabet.
        If the FSM is non-deterministic, this function does not return the epsilon symbol.
        If you actually actually want the alphabet with the epsilon, use self.alphabet
        """
        from NFA import NFA
        if isinstance(self,NFA):
            return self.alphabet - {self.EPSILON}

        return self.alphabet

    def get_transition_table(self):
        """Build the transition table from the function self.delta defined on [state] X [alphabet] -> ([state])*.
        Returns a dictionnary of states where each element is a dictionnary with (key,value) = symbol in inpute, resulting state(s)



        """
        d = {}
        for x in sorted(self.states):
            d[x] = {}
            for c in self.alphabet:
                d[x][c] = self.delta(x, c)

        return d

    def accepted_under(self, max_length):
        """
        Try all words of length smaller than input and return the list of those accepted.
        """
        accepted_words_list = []
        if self.recognizes(''):
            accepted_words_list.append('');

        for x in range(1, max_length):
            for i in product(self.getAlphabet(), repeat=x):
                entree = ''.join(i)
                if self.recognizes(entree):
                    accepted_words_list.append(entree)

        return accepted_words_list


    def accepted_under_word(self, max_word):
        """Enumerate all the accepted word. Which does not makes much sense
         when the alphabet is a unordered set of element.
        """

        accepted_words_list = []
        for x in range(1, len(max_word) + 1):
            for i in product(self.getAlphabet(), repeat=x):
                entree = ''.join(i)
                if self.recognizes(entree):
                    accepted_words_list.append(entree)
                if entree == max_word:
                    break

        return accepted_words_list

#
# Administrative functions:
#

    def prettyprint(self):
        """Displays all information about the FSM in an easy-to-read way. Not
        actually that easy to read if it has too many states.
        """
        print("")
        print("This FSM has %s states" % len(self.states))
        print("Type : "+str(type(self)))
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Starting state:", self.start)
        print("Accepting states:", self.accepts)
        print("Transition function:")
        print("\t","\t".join(map(str, sorted(self.states))))
        for c in self.alphabet:
            results = map(lambda x: self.delta(x, c), sorted(self.states))
            print(c, "\t", "\t".join(map(str, results)))
        print("Current state:", self.current_state)
        print("Currently accepting:", self.status())
        print("")

    def prettyprint2(self):
        """Alternative print. Easier to read."""
        def str2(x):
            t = type(x)
            if t == set or t == frozenset or t == list:
                return '('+''.join([str(y)+", " for y in x])[:-2]+')'
            else : return str(x)

        print("")
        print("This FSM has %s states" % len(self.states))
        print("Type : "+str(type(self)))
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Starting state:", str2(self.start))
        print("Accepting states:", self.accepts)
        print("Transition table:")

        tmp = "{"
        transition_table = self.get_transition_table()
        for x in sorted(self.states):
            tmp += str2(x)+":{"+", ".join([str(c)+":"+'{'+', '.join([str2(transition_table[x][c])])+'}' for c in self.alphabet])+"},\n"
           # tmp += str2(x)+":{"+", ".join([str(c)+":"+str2(transition_table[x][c]) for c in self.alphabet])+"},\n"
        tmp = tmp[:-2]+"}"

        print(tmp)

        print("Current state:", str2(self.current_state))
        print("Currently accepting:", self.status())
        print("")

def save_machine(FA, path):
    """Saves a single automaton using Pickle"""

    FA = FA.copy()

    # Pickle cannot serialize lambda functions. We will instead serialize a transition table of the function.
    FA.delta = FA.get_transition_table()
    f = open(path, 'wb')
    p = pickle.Pickler(f, 2)
    p.dump(FA)
    print("Saved object at " + f.name)


def load_machine(path):
    """ Loads a single automaton using Pickle"""
    FA = pickle.load(open(path, 'rb'))
    d = FA.delta.copy()

    # Make the transition table a lambda function.
    FA.delta = lambda x, c: d[x][c]

    return FA



