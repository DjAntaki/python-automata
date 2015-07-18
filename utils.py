#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
from itertools import product
from NFA import NFA
from DFA import DFA
# Some small utils

def get_transition_table(func, states, alphabet):
    """
    Build a transition table for func, a function such [states] X [alphabet] -> [states]
    Returns a dictionnary of states where each element is a dictionnary with (key,value) = [alphabet],[states]
    """


    d = {}
    for x in sorted(states):
        d[x] = {}
        for c in alphabet:
            d[x][c] = func(x, c)
            #        d[x].update(map(lambda c: (c,func(x, c)), alphabet.copy()))
    return d


def save_machine(FA, path):
    "Saves a single automaton"

    FA = FA.copy()



    # Pickle cannot serialize lambda functions. We will instead serialize a transition table of the function.
    if type(FA) == NFA:
        FA.delta = get_transition_table(FA.delta, FA.states, FA.alph_with_epsilon)
    elif type(FA) == DFA:
        FA.delta = get_transition_table(FA.delta, FA.states, FA.alphabet)
    else :
        print("Unrecognized input.")
        raise Exception

    f = open(path, 'wb')
    p = pickle.Pickler(f, 2)
    p.dump(FA)
    print("Saved object at " + f.name)


def load_machine(path):
    """ Loads a single automaton """
    FA = pickle.load(open(path, 'rb'))
    d = FA.delta.copy()

    # Make the transition table a lambda function.
    FA.delta = lambda x, c: d[x][c]

    return FA


#
# TODO : Peut-être faire une classe plus générale pour les finites states machines? Ça pourrait être pas mal puisque DFA et NFA partagent certaines foncitons
# TODO : Renommer ces fonctions.
def accepted_words_under_max_length(FA, max_length):
    """Try all words of length <=Prints the accepted words that"""
    accepted_words_list = []
    for x in range(1, max_length):
        for i in product(FA.alphabet, repeat=x):
            entree = ''.join(i)
            if FA.recognizes(entree):
                accepted_words_list.append(entree)

    return accepted_words_list


def accepted_words_under_word(FA, max_word):
    """Try all words of before in the alphabetical enumeration and return the accepted words"""
    accepted_words_list = []
    for x in range(1, len(max_word) + 1):
        for i in product(FA.alphabet, repeat=x):
            entree = ''.join(i)
            if FA.recognizes(entree):
                accepted_words_list.append(entree)
            if entree == max_word:
                break

    return accepted_words_list


def remap(FA, q0, a, q):
    """
    This function changes the output of one transition
    FA : a finite state machine
    q0 : the initial state
    a : a symbol of the alphabet
    q : the final states. Can be an object or a set of objects

    q0 -a-> set([q])
    """

    assert q0 in FA.states
    assert q in FA.alphabet
    assert q0 <= FA.alphabet

    table = get_transition_table(FA.delta, FA.states, FA.alphabet)
    table[q0][a] = q

    FA.delta = lambda x,c : table[x][c]




