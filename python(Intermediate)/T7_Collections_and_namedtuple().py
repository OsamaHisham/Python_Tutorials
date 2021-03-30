# A basic example on the nametuple module from Collections

import collections
from collections import namedtuple

point = namedtuple('Point', 'x y z')

newP = point(3, 4, 5)
print(newP)

# Eg.2 :
point = namedtuple('Point', 'x gy zc h')

newP = point(3, 4, 5, 8)
print(newP)

# An example on the nametuple with a list

point = namedtuple('Point', ['x', 'y', 'a'])

newP = point(3, 4, 5)
print(newP)

# An example on the nametuple with a dictionary

point = namedtuple('Point', {'x':0, 'y':0, 'z':0})

newP = point(3, 4, 5)
print(newP)

# --- Other interesting features as well and features that goes with nametuple :

  # -- here it allows us to acces each element by its' index ( name ) which can't be done by a regular tuple.
point = namedtuple('Point', {'x':0, 'y':0, 'z':0})

newP = point(3, 4, 5)
print(newP.x, newP.y, newP.z)

  # -- We can also use the same operation that we use on basic tuples as well.
print(newP[0])

  # -- Printing it in the form of a dictionary.
print(newP._asdict())

  # -- Printing field names as well if you want to get them.
print(newP._fields)


  # -- using a method called the replace method
     # --- so here it means we want to replace the value of y to 8 inside of the namedtuple,
     # --- but we can't do that by using the _replace method alone as this function is not
     # --- capable of changing the tuple object, so we have to assign a new varibale / object to it
     # --- and what that will do it returning a new named tuple to our pre-existing one,
newP = newP._replace(y = 8)
print(newP)

# -- last method (_make) is assigning elements to our named tuple accordingly
p2 = point._make (['a', 'b', 'c'])
print(p2)