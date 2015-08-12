__author__ = 'ntak'
import NFA

"""
This regex accepts any word w composed of a and b that has |a|%2=0 |b|%4=0
>>> nfa = regexToNFA('(b*(ab*ab*)*|a*(ba*ba*ba*ba*)*)')

"""

def _tree_from_regex(regex):
    """
    Takes an regex in form of a string

    Alphabet : single characters that aren't used as operators.
    Supported operations : '(x)', 'x*', 'x+', 'x|y', 'xy'

    :param regex: a string containing a regular expression (only with supported operations)
    :return: a tree representing the regex from in a prefix manner.
    """

    parentheses = []
    counter = 0
    open = None
    for e, char in enumerate(regex):
        if char == '(':
            counter += 1
            if counter == 1:
                open = e
            elif counter < 1:
                raise Exception

        elif char == ')':
            if counter == 1:
                counter -= 1
                parentheses.append((open, e))

            elif counter > 1:
                counter -= 1
                pass
            else:
                raise Exception

    assert counter == 0


    #There is a priority of operations to respect with regex
    #
    # 1. (x)
    # 2. x+, x*
    # 3. xy
    # 4. x|y

    # 1. the (x) operation

    r = []
    last = -1  # the index of the last ) met iterating in parentheses.
    for i, j in parentheses:
        if last + 1 < i:
            r.append(regex[last + 1:i])
        r.append(_tree_from_regex(regex[i + 1:j]))
        last = j

    if last < len(regex) - 1:
        r.append(regex[last + 1:])

    # 2. the *, + operations
    operators = {'*', '+'}
    r2 = []

    for e in r:
        if type(e) is str and any(i in operators for i in e):
            new_e = ''
            for char in e:
                if char in operators:
                    if new_e == '':
                        x = len(r2)
                        assert x > 0
                        if not r2[x - 1] is None:
                            r2[x - 1] = (char, r2[x - 1])
                    else:
                        x = len(new_e) - 1
                        t = new_e[x]
                        if x > 0:
                            r2.append(new_e[:x])
                        r2.append((char, t))
                        new_e = ''
                else:
                    new_e += char
            if not new_e == '':
                r2.append(new_e)
        else:
            r2.append(e)

    # 3. Concatenation (and the or operation)
    r3 = []
    c = False
    concat = []
    or_stack = []
    for e in r2:
        if type(e) is str:
            for char in e:
                if char == '|':
                    x = len(concat)
                    if x > 1:
                        or_stack.append(('concat', concat))
                    elif x == 1:
                        or_stack.append(concat[0])
                    elif x == 0:
                        or_stack.append(None) #epsilon
                    concat = []

                else:
                    concat.append(char)

        elif e is not None:
            concat.append(e)
    #just one more iteration.
    x = len(concat)
    if x > 1:
        or_stack.append(('concat', concat))
    elif x == 1:
        or_stack.append(concat[0])
    elif x == 0:
        or_stack.append(None) # epsilon

    if len(or_stack) > 1:
        r3.append(('|', or_stack))
    else:
        #There is no or in the regex at this level
        r3.append(or_stack[0])

    if len(r3) == 1:
        return r3[0]
    return r3



state_counter = None
previous = None
alphabet = None
delta = None
def regexToNFA(regex):
    """

    :param regex: a regex that defines a language.
    Supported operations : '('+x+')', 'x*', 'x+', 'x|y', 'xy'
    Alphabet : single characters that aren't used as operators.
        ex. (a(bbc|d)*) , 10(101|000)*01(0|1)+

    :return: the non-deterministic automaton that describe that language.
    """

    global state_counter
    global previous
    global alphabet
    global delta
    x = _tree_from_regex(regex)
#    print(x)
    state_counter = -1
    states = set()
    delta = {}

    def new_state():
        global state_counter
        state_counter += 1
        i = "x_%i" % state_counter
        states.add(i)
        delta[i] = {}
        return i

    def add(dictionnary, key, addvalue):
        if key in dictionnary.keys():
            dictionnary[key].add(addvalue)
        else:
            dictionnary[key] = set([addvalue])

    epsilon = 'epi'
    alphabet = set([epsilon])
    start = new_state()
    previous = start


    def parse_tree(expr):
        global previous
        global alphabet
        global delta

        if len(expr) == 1 :
            n = new_state()
            add(delta[previous], expr, n)
            alphabet.add(expr)
            previous = n

        elif expr[0] == '*':

            initial = previous
            previous = new_state()
            add(delta[initial], epsilon, previous)
            parse_tree(expr[1])
            add(delta[previous], epsilon, initial)
            previous = new_state()
            add(delta[initial], epsilon, previous)

#            add(delta[previous], epsilon, i)
#            previous = i
#            parse_tree(expr[1])
#            final = previous
#            add(delta[final], epsilon, i)
#            add(delta[i], epsilon, final)


        elif expr[0] == '+':
            initial = previous
            parse_tree(expr[1])
            final = previous
            add(delta[final], epsilon, initial)

        elif expr[0] == '|':
            initial = previous
            end = []
            for e in expr[1]:
                previous = new_state()
                add(delta[initial], epsilon, previous)
#                previous = initial
                parse_tree(e)
                end.append(previous)

            final = new_state()
            for i in end:
                add(delta[i], epsilon, final)
            previous = final

        elif expr[0] == 'concat':
            for e in expr[1]:
                parse_tree(e)

    parse_tree(x)
    for s in states:
        k = delta[s].keys()
        delta[s].update({i: None for i in filter(lambda x: not x in k, alphabet)})

#    print(states, alphabet, delta, start, previous, epsilon)
    return NFA.NFA(states, alphabet, lambda x, c: delta[x][c], start, [previous], epsilon)

def test1():
    automaton = regexToNFA('((aa)*|(bbb)*)+')
    assert automaton.recognizes('aa') is True
    assert automaton.recognizes('') is True
    assert automaton.recognizes('bbb') is True
    assert automaton.recognizes('bbbbbb') is True
    assert automaton.recognizes('aabbbaa') is True
    assert automaton.recognizes('ab') is False
    assert automaton.recognizes('aabbbbaa') is False
    assert automaton.recognizes('a') is False
    #    print(automaton.accepted_under_length(10))
    return automaton


def test2():
    return regexToNFA('a*(a|bb)+')
    assert automaton.recognizes('a') is True
    assert automaton.recognizes('aa') is True
    assert automaton.recognizes('bb') is True
    assert automaton.recognizes('aabbabbabba') is True
    assert automaton.recognizes('bbbbbbaa') is True
    assert automaton.recognizes('ab') is False
    assert automaton.recognizes('baaaa') is False
    assert automaton.recognizes('') is False
 #   print(automaton.accepted_under_length(10))
    return automaton


def test3():
    automaton = regexToNFA('(c(a|b(ab|cd)*))*')
    automaton.pretty_print()
    assert automaton.recognizes('ca') is True
    assert automaton.recognizes('cbabcdabab') is True
    assert automaton.recognizes('cb') is True
    assert automaton.recognizes('') is True
    assert automaton.recognizes('cba') is False
    assert automaton.recognizes('cbcacbcb') is True
    assert automaton.recognizes('cbcabacdb') is False
#   print(automaton.accepted_under_length(10))
    return automaton


def test4():
    automaton = regexToNFA('(c|b)(abc)*(a|a(ab|cd)*e+|ec*e)')
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
    #    print(automaton.accepted_under_length(10))
    return automaton

#test3()