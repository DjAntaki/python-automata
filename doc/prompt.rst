Prompt Interface
================

To run the interactive prompt interface, use one of the two following command :

 | .../python_automata$ python -i src/prompt2.py
 | .../python_automata$ python3 -i src/prompt.py


You can then call one of the two prompt function (dfa_input or nfa_input). Those function return respectively a deterministic and a non-deterministic finite automaton.

 | >>> dfa1 = dfa_input()

 | >>> nfa1 = nfa_input()

The instructions given by the prompt should be sufficient for good use.

.. automodule:: prompt
   :members: