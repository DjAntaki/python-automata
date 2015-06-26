from NFA import NFA

etats = {0,1,2,3,4}
alphabet = {'a','b','c'}

d = [{'a':0,'b':2,'c':2,'epi':4},
{'a':set([1,4]),'b':None,'c':None, 'epi':None},
{'a':None,'b':3,'c':set([3,4]), 'epi':None},
{'a':set([0,1]),'b':None,'c':2,'epi':4},
{'a':None,'b':None,'c':None,'epi':None}]
accept =  set([4])
start = 0
#def delt(state,symbol):
#    if symbol == 'a':
#        return state + 1 % 5
#    elif symbol == 'b':
#        return state + 4 % 5
#    else :
#        return state


test_nfa = NFA(etats,alphabet,lambda x,y: d[x][y],start,accept)

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
