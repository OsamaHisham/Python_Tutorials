# Collections deque
  # --- It can be used in the same way as a list but it's more reliable and faster.

import collections
from collections import deque

# Basic example for a deque
d = deque('hello')
print(d)

# Using the append method to add elements to the list :
d.append('4')       # --- adding an element to the end
d.appendleft(5)   # --- adding an element to the start
print(d)

# Using the pop method to remove elements to the list :
d.pop()       # --- removes the first element
d.popleft()   # --- removes the last element
print(d)

# Using the clear method to remove all the elements from the deck :
d.clear()
print(d)

# Using the extend method that takes an iterable argument like a (list , string )
# and puts it at the end of the list
d.extend('456')       # --- adding a sting to the empty deck from last example
d.extend([1, 2, 3])   # --- adding a list to the end of the deck list
d.extendleft('hey')       # --- adding a sting to the start of the deck list and in reverse order ('y' , 'e' , 'h')
print(d)

# Using the rotate method which is better if you are dealing with things at the beginning or end specifically :
   # --- it take either a +ve or -ve integer . +ve rotates it to the right and -ve to the left.
   # --- which means a -ve value shits all of the elements one place to the left
   # --- and a +ve value shits all elements to the right
d.rotate(-1)
print(d)

# A really useful thing to apply to these decks as well is the (maxlen) :
p = deque('hello', maxlen = 5)
print(p)
p.append(1)   # --- adding an element

   # --- so here what is going to happen is that the first element will be removed
   # --- in order to maintain the maximum length of 5 elements that was set
print(p)
