Credits
=======

Credits to andrewbar for the initial code for the DFA. I found his 2008 project named "python-automata" on google code (code.google.com/p/python-automata). The project already supported deterministic finite automaton (DFA), minimisation algorithms, cross products between DFAs and much more.

I've added :

- a non-deterministic finite automaton (NFA) class that supports simulation
- an abstracted a Finite Automaton class that is herited by both DFA and NFA
- added functions to enumerate accepted words and a second pretty_print function
- added an algorithm to create a DFA from a NFA
- added a parser that takes a regex in input and that returns a NFA
- Added a prompt to create NFAs and DFAs.

For bug report or other inquieries :
https://github.com/DjAntaki/python_automata

antaki.vincent@gmail.com


Link to the initial python-automata by andrewbar : (code.google.com/p/python-automata)
