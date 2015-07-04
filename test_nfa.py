#!/usr/bin/python
# -*- coding: utf-8 -*-

import DFA
from NFA import NFA
from itertools import product

verbose = False

def test1():
    ##un peu messy comme test

    etats = {0,1,2,3,4}
    alphabet = {'a','b','c'}

    d = [{'a':0,'b':2,'c':2,'epi':4},
    {'a':set([1,4]),'b':None,'c':None, 'epi':None},
    {'a':None,'b':3,'c':set([3,4]), 'epi':None},
    {'a':set([0,1]),'b':None,'c':2,'epi':4},
    {'a':None,'b':None,'c':None,'epi':None}]
    accept =  set([4])
    start = 0


    test_nfa = NFA(etats,alphabet,lambda x,y: d[x][y],start,accept)

    #Some words to test.
    assert test_nfa.recognizes('') is True
    assert test_nfa.recognizes('a') is True
    assert test_nfa.recognizes('aaaaaaaaaaaaaa') is True
    assert test_nfa.recognizes('aaa') is True
    assert test_nfa.recognizes('ab') is False
    assert test_nfa.recognizes('ac') is False
    assert test_nfa.recognizes('bc') is True
    assert test_nfa.recognizes('cc') is True
    assert test_nfa.recognizes('bccbcc') is True
    assert test_nfa.recognizes('bccc') is True
    assert test_nfa.recognizes('cbcc') is True
    assert test_nfa.recognizes('ba') is False
    assert test_nfa.recognizes('abc') is True
    assert test_nfa.recognizes('aaabccccb') is True
    assert test_nfa.recognizes('abba') is True
    assert test_nfa.recognizes('abbaaaaaaaaaaaaaaaaaaa') is True
    assert test_nfa.recognizes('abbac') is False
    assert test_nfa.recognizes('abbab') is False

    return test_nfa

def test2():
    #Example tiré des notes de cours de Pierre Mckenzie pour le cours IFT2105

    #NFA that accepts words with |w|_a = 0 mod 2 or |w|_b = 0 mod 4

    etats = set(["a_%i" % (i) for i in range(2)]).union(["b_%i" % i for i in range(4)])
    etats.add('e')
    alphabet = ['a','b']

    start = 'e'
    accept = set(['a_0','b_0'])

    def delt(state,symbol):
        print(state, symbol)
        if(state[0] == 'a' ):
            if (symbol == 'a'):
                return 'a_'+str((int(state[2])+1) % 2)
            elif (symbol == 'b'):
                return state
            else :
                return None
        elif(state[0] == 'b'):
            if (symbol == 'a'):
                return state
            elif (symbol == 'b'):
                return 'b_'+str((int(state[2])+1) % 4)
            else :
                return None
        elif(state == 'e'):
            if (symbol == 'epi'):
                return set(['a_0','b_0'])
            else :
                return None

    nfa = NFA(etats,alphabet,delt,start,accept)

    dfa = nfa.build_DFA_from_NFA()
    print("qweqwe")
    #Ok next is an equivalent DFA resulting of the union of
    # the DFA that accepts only (|w|_a = 0 mod 2) and
    # the DFA that accepts only (|w|_b = 0 mod 4)

    etats2a = set(["a_%i" % (i) for i in range(2)])
    etats2b = set(["b_%i" % i for i in range(4)])

    def delt2a(state, symbol):
        assert state[0] == 'a'
        if (symbol == 'a'):
            return 'a_'+str((int(state[2])+1) %2)
        elif (symbol == 'b'):
            return state
        else :
            return None


    def delt2b(state, symbol):
        assert state[0] == 'b'
        if symbol == 'b':
            return 'b_'+str((int(state[2])+1) % 4)
        elif symbol == 'a':
            return state
        else :
            return None

    dfa2a = DFA.DFA(etats2a, alphabet, delt2a, 'a_0', ['a_0'])
    dfa2b = DFA.DFA(etats2b, alphabet, delt2b, 'b_0', ['b_0'])
    dfa2 = DFA.union(dfa2a,dfa2b)

    #Time to test!
    to_test = [nfa,dfa,dfa2]
    verbose = False
    print("121")
    results = [x.recognizes('') for x in to_test]
    assert all(results) is True
    verbose = True
    for x in range(1,10):
        for i in product(alphabet, repeat=x):
            entree = ''.join(i)
            if verbose : print(entree)
           # if entree=='abbbb':  import ipdb;ipdb.set_trace()
            results = [y.recognizes(entree) for y in to_test]
            if verbose : print(results)
            if entree.count('a') % 2 == 0 :
                assert all([r is True for r in results])
            elif entree.count('b') % 4 == 0 :
                assert all([r is True for r in results])
            else :
                assert all([r is False for r in results])
                
    return to_test
test1()
a = test2()

"""
epsilon = 'epi'
alphabet = ['a']
states = range(5)

def delt(state, symbol):
    if symbol == 'epi':
        if state == 0:
            return 4
    if state == 0:
        if symbol =='a':
            return 

x = NFA()
"""
