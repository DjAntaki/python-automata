DFA
===

Example
-------

Here is an example of an initialisation of a DFA that accepts
the language (bab)*baa

 | >>> states = [0,1,2,3]
 | >>> alphabet = ['a','b']
 | >>> accepts = {3}
 | >>> start = 0
 | >>> transition_table = {0:{'a':None,'b':1}, 1:{'a':2,'b':None}, 2:{'a':3,'b':0},3:{'a':None,'b':None}}
 | >>> delta = lambda s,a : transition_table[s][a]
 | >>> dfa = DFA(states, alphabet, delta, start, accepts)
 | >>> dfa.prettyprint2()
 |
 | This FSM has 4 states
 | Type : <type 'instance'>
 | ('States:', set([0, 1, 2, 3]))
 | ('Alphabet:', set(['a', 'b']))
 | ('Starting state:', '0')
 | ('Accepting states:', set([3]))
 | Transition table:
 | {0:{a:{None}, b:{1}},
 | 1:{a:{2}, b:{None}},
 | 2:{a:{3}, b:{0}},
 | 3:{a:{None}, b:{None}}}
 | ('Current state:', '0')
 | ('Currently accepting:', False)
 |
 | >>> dfa.accepted_under(10)
 | ['baa', 'babbaa', 'babbabbaa']


Documentation
-------------

.. automodule:: DFA
   :members:
   :undoc-members:
   :private-members:
   :special-members:
   :inherited-members:
