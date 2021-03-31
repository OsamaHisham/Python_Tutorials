# optional parameters

# Normal way to define a function and assign parameters to it :
def func(x):
    return x ** 2

call = func(5)
print(call)

# Creating an optional parameter for the defined function :

   # --- It allows you to assign a value to the parameter of the defined function
   # --- and when the optional parameter method it used there is no need to palce
   # --- a value for the optional parameter stated when the function is called
def func(y = 1):     # --- optional parameter (y)
    return y ** 2

call2 = func()       # --- calling the function that has the optional parameter
print(call2)

# Creating an optional parameter for the defined function (calling the function):

   # --- If a value is placed inside the function when calling it that value
   # --- will replace / rewrite the original value that was assigned.
def func(y = 1):     # --- optional parameter (y)
    return y ** 2

call2 = func(5)       # --- calling the function and modifying the value of the parameter y to 3
print(call2)

# using optional parameters with normal parameters together :
def func(word, freq = 2):     # --- normal parameter (word) & optional parameter (freq)
    print(word * freq)

call3 = func('Jack')       # --- calling the function and defining the word parameter only as freq is an optional parameter

# using multiple optional parameters with normal parameters together :
    # --- normal parameter (word) & optional parameters (freq) , (add)
def func(word, add = 5, freq = 1):
    print(word * (freq + add))

    # --- calling the function and defining the word parameter only as freq and add are optional parameters
call3 = func('Hello')
    # --- calling the function and defining the word parameter + changing the optional parameter add to 0
call3 = func('Hello', 0)
    # --- calling the function and defining the word parameter + changing the optional parameters (add to 5) , (freq to 1 )
call3 = func('Hello', 5 , 3)


# A practical example of how this can be useful while writing a program :
    # --- defining a new class called car
class car(object):
    def __init__(self, make, model, year, condition = 'New', kms = 0):    # --- so here the optional parameters that was choosen are (condition) and ( kms)
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll = True):    # --- for this second function the optional parameter set was (showAll)
        if showAll:
            print('This car is %s %s from %s, it is %s and has %s kms.'%(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print('This car is a %s %s from %s.'%(self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2012)    # --- Here only the parameters (make), (model), (year) where defined as the rest are optional parameters
whip.display()    # --- For the display function it has just one parameter that is an optional parameter so nothing was writen while calling it
whip.display(False)    # --- I changed the optional parameter set, from the value of ( True ) to be ( False )

