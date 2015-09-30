# python_automata

Librairy in python to manipulate deterministic and non-deterministic finite automata (from now on referenced has DFA and NFA or finites automata). 

Supports :
- Simulation of DFA and NFA exection step by step or over an iterable sequence
- Validation of the definition of a finite automata. 
- Creating a NFA from a limited regex expression (operators supported in priority order : (),+,*, concatenation and |)
- Creating DFA from NFA
- Multiple minimization algorithms for DFA
- generalized cross-product operation between DFA (including union, intersection, symmetric difference)
- 

See file doc/index.html for complete documentation and examples.

The vast majority of the code of DFA.py comes from andrewb :
code.google.com/p/python-automata
