# Filter Function :

def add7(x):
    return x+7

def isOdd(x):
    return x%2 !=0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter function:
# --- It takes the same arguments as the map function
# --- which are ( function defined , list defined )
b = list(filter(isOdd, a))

# Filter + map functions together:
# --- using the map function and adding the
# --- list b that has been filtered inside it
c1 = list(map(add7, b))

# Or we can save a line by directly adding list b inside
# and removing the list() at the start for the conditions of b
c2 = list(map(add7, filter(isOdd, a)))