# --- How python code actually runs and why the weird lines mentioned bellow will work with python.

""" python runs the code by first compiling it and then the code is interpreted.

    So what does a compiler do ?
    A compiler take a high level code and translates it to a lower level ( Byte code )
    which is a little harder for us to understand and closer for the machine to understand and run.

    What does an interpreter do ?
    It takes some kind of code, typically a byte code, and interprets and runs that code.
    So it will read that code and translate it on the fly into into machine code that
    can be executed by our computer rather than doing this translation before hand.


    The way python execution chain when the code is run :

    First, the high level code is written by you and stores on your desktop and then you go to execute that code
    what happens is that it's translated to something called byte code.
    This translation is basically a tool that checks all of the syntax for your python code and converts it into some
    equivalent code that can be read by the interpreter that we are going to use.

    When there is an invalid syntax in our code for example, what happens is that we get an error because the
    translation can't happen as the format of our code is incorrect and hence invalid syntax.

    Assuming that our syntax is correct then what happens is that you will mov on to the next stage where everything
    will be translated into byte code and then that byte code will run through the compiler and the compiler will translate
    that byte code into live time into machine code that runs and executes on your machine.
"""


class Dog:
    def __init__(self):
        self.bark()
''' When this simple example shown above is executed it runs normally, even though the method sel.bark does not exist in the 
    class body.
    Now this code runs on our machine what happens, and that is something unique to python, is that our code is only 
    executed at run time and not at compile time. 
    All that the compiler does for us is just translate that code into byte code and it doesn't check if the code is valid. 
'''

def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)
    return Dog   # --- Notice that here I return Dog itself which is actually a reference to class and not the object.

cls = make_class(10)
print(cls)
print('')
''' So what have I actually done inside this function though ? 
    Well, I created a class that uses the value from the actual function argument here and we actually returned the class
    itself and not an instance of that class. 
    Now, we can run this on python as what python will do is tore all of these things that we defined here are actually being
    stored in memory. 
    So the (Dog) class actually has a memory location for it and that's what is being shown by the terminal when it runs and 
    the same thing applies for our (make_class) function as well as out (cls) variable and with anything else that we define.
'''

# --- So can we use this ?
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)
    return Dog   # --- Notice that here I return Dog itself which is actually a reference to class and not the object.

cls = make_class(10)
d = cls('Tim')
print(d.name)
d.print_value()
print('')
''' Here what I have done is said okay the (cls) variable is actually a class and since it's a class what I can do is use 
    is use it in the same way that I would typically use a class. It's literally another name for (Dog). 
    So I put a bracket and created an instance for it which is stored in the (self.name).
    And what we will do is call the method on our object now that prints the value that we gave when we we actually
    created this. 
'''

# --- Another example using a different kind of syntax:
for i in range(10):
    def show():
        print(i*2)
    show()
show()
print('')
''' Here I defined a function inside of a for loop. 
    what I have done here is, well only one (show) will even exist at the end of this kind of run time
    But here because it is inside a for loop it essentially means that i have defined 10 different (show's) that do 10 
    different things and I called them directly after and then they get overwritten and I do them again when it is called 
    inside of the for loop. 
    However, When calling the (show) function outside of the for loop only one value will be printed which is (18) 
    the last value.
'''

# --- Another example :
def func(x):
    if x == 1:
        def rv():
            print('X is equal to 1')
    else:
        def rv():
            print('X is not 1 ')
    return rv

new_func = func(1)
new_func()
new_func = func(10)
new_func()
print('')

# --- Example to look into some of the details of our objects :
import inspect

def func(x):
    if x == 1:
        def rv():
            print('X is equal to 1')
    else:
        def rv():
            print('X is not 1')
    return rv

new_func = func(2)
print(id(new_func))
print('')
print(inspect.getmembers(new_func))
print('')
print(inspect.getsource(new_func))
''' When we print out this it should give us the memory address which is the location of our function.

    The inspect module that I imported above can show us a variety of things because of the fact that our python 
    (objects, classes ) and all of that are actually live and we interact with them and inspect them and we can 
    ask questions about them and get that value back from the interpreter.
    [1] the .getmembers gives you a variety of information that you can use as well as the location for each one of them.
    [2] .getsource provides you with the source code for whatever you want.
'''

