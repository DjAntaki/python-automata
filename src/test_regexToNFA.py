__author__ = 'ntak'

from regexToNFA import regexToNFA as r

def test1():
    #Basic operations
    nfa = r('a|b')
    assert nfa.recognizes('') is False
    assert nfa.recognizes('a') is True
    assert nfa.recognizes('b') is True
    assert nfa.recognizes('aa') is False
    assert nfa.recognizes('bb') is False

    nfa = r('ab')
    assert nfa.recognizes('') is False
    assert nfa.recognizes('a') is False
    assert nfa.recognizes('b') is False
    assert nfa.recognizes('aa') is False
    assert nfa.recognizes('bb') is False
    assert nfa.recognizes('ab') is True
    assert nfa.recognizes('aab') is False

    nfa = r('a*')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('a') is True
    assert nfa.recognizes('aaaa') is True

    nfa = r('a+')
    assert nfa.recognizes('') is False
    assert nfa.recognizes('a') is True
    assert nfa.recognizes('aaaa') is True

    #Epsilon
    nfa = r('')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('a') is False

    nfa = r('a|')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('a') is True

    nfa = r('()*')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('a') is False
    nfa = r('()+')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('a') is False

    #Somecases
    nfa = r('ab*(a|aa)b*(c|)')
    assert nfa.recognizes('aa') is True
    assert nfa.recognizes('') is False
    assert nfa.recognizes('abbbbbbbaabc') is True
    assert nfa.recognizes('aaabb') is True
    assert nfa.recognizes('aabb') is True
    assert nfa.recognizes('aabbc') is True
    assert nfa.recognizes('abbaac') is True
    assert nfa.recognizes('abbaabbbc') is True
    assert nfa.recognizes('abbaabac') is False

    nfa = r('((aa|(ab)*|(c|))+|a)')
    assert nfa.recognizes('') is True
    assert nfa.recognizes('aaabc') is True
    assert nfa.recognizes('aac') is True
    assert nfa.recognizes('') is True
    
    

def test2():
    return r('a*(a|bb)+')
    assert automaton.recognizes('a') is True
    assert automaton.recognizes('aa') is True
    assert automaton.recognizes('bb') is True
    assert automaton.recognizes('aabbabbabba') is True
    assert automaton.recognizes('bbbbbbaa') is True
    assert automaton.recognizes('ab') is False
    assert automaton.recognizes('baaaa') is False
    assert automaton.recognizes('') is False
 #   print(automaton.accepted_under(10))
    return automaton


def test3():
    automaton = r('(c(a|b(ab|cd)*))*')
    assert automaton.recognizes('ca') is True
    assert automaton.recognizes('cbabcdabab') is True
    assert automaton.recognizes('cb') is True
    assert automaton.recognizes('') is True
    assert automaton.recognizes('cba', True) is False
    assert automaton.recognizes('cbcacbcb') is True
    assert automaton.recognizes('cbcabacdb') is False
    return automaton


def test4():
    automaton = r('(c|b)(abc)*(a|a(ab|cd)*e+|ec*e)')
    assert automaton.recognizes('ca') is True
    assert automaton.recognizes('cabcaabca') is False
    assert automaton.recognizes('cabcaabcde') is True
    assert automaton.recognizes('babcaabcdcdabeeeeeeeeeeeeeee') is True
    assert automaton.recognizes('baabcde') is True
    assert automaton.recognizes('aabcd') is False
    assert automaton.recognizes('ab') is False
    assert automaton.recognizes('baaaa') is False
    assert automaton.recognizes('cecec') is False
    assert automaton.recognizes('') is False
    assert automaton.recognizes('bbcae') is False
    assert automaton.recognizes('becccccce') is True
    assert automaton.recognizes('bee') is True
    #    print(automaton.accepted_under(10))
    return automaton

def test5():
    automaton = r('((aa)*|(bbb)*)+')
    assert automaton.recognizes('aa') is True
    assert automaton.recognizes('') is True
    assert automaton.recognizes('bbb') is True
    assert automaton.recognizes('bbbbbb') is True
    assert automaton.recognizes('aabbbaa') is True
    assert automaton.recognizes('ab') is False
    assert automaton.recognizes('aabbbbaa') is False
    assert automaton.recognizes('a') is False
    #    print(automaton.accepted_under(10))
    return automaton

