Regex to NFA
=====

RegexToNFA File contains the procedure used to build a non-deterministic finite automaton from a regex.

Only the following basic operators are accepted with the following priority :
 1. parentheses "(x)"
 2. "x*" and "x+"
 3. concatenation "xy"
 4. or (union if you prefer) "x|y"

Here is an example of typical usage of module regexToNFA.

Let |w_a| be the number of 'a' in a word and |w_b| be the number of 'b' in the same word.
Let L be the language with the alphabet {'a','b'} that accepts words with |w_a| % 2 == 0 or |w_b| % 4 == 0.
L can be represented by the following regex "(b*ab*ab*)*|(a*ba*ba*ba*ba*)*"

We will use it to create a NFA :

 | python_automata$ python -i src/regexToNFA.py
 | >>> nfa1 = regexToNFA('(b*ab*ab*)*|(a*ba*ba*ba*ba*)*')
 | >>> nfa1.accepted_under_length(6)
 | ['','aa', 'baa', 'aba', 'aab', 'bbbb', 'bbaa', 'baba', 'baab', 'abba', 'abab', 'aabb', 'aaaa', 'bbbba', 'bbbab', 'bbbaa',
 | 'bbabb', 'bbaba', 'bbaab', 'babbb', 'babba', 'babab', 'baabb', 'baaaa', 'abbbb', 'abbba', 'abbab', 'ababb', 'abaaa',
 | 'aabbb', 'aabaa', 'aaaba', 'aaaab']
 | >>>


.. automodule:: regexToNFA
   :members: