NFA
===

Here is an example of an initialisation of a NFA that accepts
the language (b|)(a(ba)*a)+

 | >>> states = [0,1,2,3]
 | >>> alphabet = ['a','b']
 | >>> accepts = {3}
 | >>> start = 0
 | >>> epsilon = 'eps'
 | >>> transition_table = {0:{'a':None,'b':1, 'eps':1}, 1:{'a':2,'b':None, 'eps':None},
 | ...                     2:{'a':3,'b':1,'eps':None},3:{'a':None,'b':None, 'eps':1}}
 | >>> delta = lambda s,a : transition_table[s][a]
 | >>> nfa = NFA(states, alphabet, delta, start, accepts, epsilon)
 | >>> nfa.pretty_print2()
 |
 | This FSM has 4 states
 | Type : <type 'instance'>
 | ('States:', set([0, 1, 2, 3]))
 | ('Alphabet:', set(['a', 'b', 'eps']))
 | ('Starting state:', '(0)')
 | ('Accepting states:', set([3]))
 | Transition table:
 | {0:{a:{None}, b:{1}, eps:{1}},
 | 1:{a:{2}, b:{None}, eps:{None}},
 | 2:{a:{3}, b:{1}, eps:{None}},
 | 3:{a:{None}, b:{None}, eps:{1}}}
 | ('Current state:', '(0, 1)')
 | ('Currently accepting:', False)
 |
 | >>> nfa.accepted_under(10)
 | ['aa', 'baa', 'aaaa', 'abaa', 'baaaa', 'babaa', 'aaaaaa', 'aaabaa', 'abaaaa', 'ababaa', 'baaaaaa', 'baaabaa', 'babaaaa', 'bababaa', 'aaaaaaaa', 'aaaaabaa', 'aaabaaaa', 'aaababaa', 'abaaaaaa', 'abaaabaa', 'ababaaaa', 'abababaa', 'baaaaaaaa', 'baaaaabaa', 'baaabaaaa', 'baaababaa', 'babaaaaaa', 'babaaabaa', 'bababaaaa', 'babababaa']

.. automodule:: NFA
   :members:
   :undoc-members:
   :private-members:
   :special-members:
   :inherited-members:
