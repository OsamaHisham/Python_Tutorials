# Map Function ( basic method ):

# allows us to apply a function to the list and then create
# a new list with those new values.

# Example of a problem
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x
# Using the map function:
# ---map takes 2 arguments ( function name , list name )
# ---what it does is it applies the function on
# ---each element in the list
#print(list(map(func, li)))
# another method as well called ( list comprehension ):
# --- it takes the function(x) and apply it for every
# --- value of x in the list and because of the
# --- [ ] brackets it turns into a list
print([func(x) for x in li])

# --- Can also add an expression as well.
print([func(x) for x in li if x%2==0])