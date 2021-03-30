# 6 collections

# --- It's a built in function that allows
# --- us to have different data types to that we can store
# --- info. or sort through info and do other things.

import collections
from collections import Counter

# Containers: A term in python and they are a data type or an object that stores multiple objects like;
  # -- list ---   # --- set ---   # --- dict ---   # --- tuple -> inmuttable ---

# Collections are just like containers but they have their own methods and other things you can do wih them
  # --- conter ---   <--- will be given in this Tutorial
  # --- deque ---
  # --- namedTuple() ---
  # --- orderdDict ---
  # --- defaultdict ---

# --- Examples of Count and how to use them ---
c = Counter('gallad')
print(c)
c = Counter(['a','a', 'b', 'c', 'c'])
print(c)
d = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats = 4, dogs = 7)
print(c)

# --- If we want to reference a specific item from our counter
print(c['cats'])

# --- If we place a key / reference that is not present into Count it
# --- doesn't return an error like a dictionary does. instead it gives a 0
print(c['pet'])

# --- If we for example want to list all the elements in our counter
print(list(c.elements()))

# --- Another useful method is the .most_common and inside it you can
# --- input how many elements you want to find that are the most common inside the counter
print(d.most_common(2))

# --- you can Subtract counts from using other integral objects or
# --- you can add the counts of objects to them
e = Counter(a = 4, b = 2, c = 0, d = -2)
a = ['a', 'b', 'b', 'c']
e.subtract(a)   # --- to subtract the counter elements from the list a
print(e)
e.update(a)   # --- to add the counter elements from the list a
print(e)      # --- in this print here it should give us the same counter values as we subtracted and added back the same values

# --- the .clear method which removes all the counts inside
# --- (  I will apply it to the counter e above )
e.clear()
print(e)

# --- Other interesting features as well and there are a few operations that are applied to them:
# --- Here I am going to use the counters e and a for these features

e = Counter(a = 4, b = 2, c = 0, d = -2)
a = Counter(['a', 'b', 'b', 'c'])

# 1. Adding / subtracting counters using the + sign :
print(e + a)   # --- Addition
print(e - a)   # --- Subtraction

e = Counter(a = 4, b = 2, c = 0, d = -2)
a = Counter(['a', 'b', 'b', 'c'])

# 2. Intersection and Union
print(e & a)   # --- Intersection
print(e | a)   # --- Union