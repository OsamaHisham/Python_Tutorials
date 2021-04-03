# There are 4 main data types in python :

''' {1} Integer which is denoted by [ int () ] :

     It is defined as any WHOLE number which can either be positive or negative
     Some examples:
     ( 4 ) , ( 76 ) , ( 170 ) , ( -30 ) , ( -149 )
'''
# Example in code :
int(4)
int(76)
int(170)
int(-30)
int(-149)

'''  {2} String which is denoted by [ str () ] : 

     A string is anything basically embedded with either a single quotation ( ' ) or double quotations ( " ) 
     some examples ( single quotations or double ) : 
     ( 'Tim' ) , ( 'Osama' ) , ( '4032' ) , ( "Hello" ) , ( "Welcome" )
     
     Even though there is a number above ( '4032' ) it is still considered a string as it is surrounded by Quotation marks.  
'''
# Example in code :
str('Tim')
str('Osama')
str('4032')
str("Hello")
str("welcome")

'''  {3} Boolean data types which are denoted by [ bool () ] : 
 
     is something like ( True or False ) --> these are reserved words in python and are 
     highlighted when added to indicate that.
     The words True and False MUSt start in a capital letter in order for it to be considered as a key word for the
     boolean data type.
'''
# Example in code :
bool(True)
bool(False)

'''  {4} float data type which is denoted by [ float () ]  :

     Anything decimal number with a floating point.
     some examples : 
     ( 0.59 ) , ( 0.35 ) , ( 0.5839 ) , ( 0.9 ) , ( 49.60 ) 
'''
# Example in code :
float(0.59)
float(0.35)
float(0.5839)
float(0.9)
float(49.60)

''' 
Question (1) : 

What type of data type these examples are ? 
{1} 'Hello'
{2} 123
{3} 3.22
{4} True
{5} "2"
{6} "70"
------------------------------------------------------
ANS: 
{1} String 
{2} Integer
{3} Float
{4} Boolean
{5} String
{6} String
'''


'''__( 2nd Section)__

Variables :

In math we usually tend to use (x) as a variable.
like ( x = 5 ) or ( x = 10 ) , e.t.c.
It is basically the same thing in python.
All you have to do in python to declare a variable is to type the variable name and then give it a value 
E.g : 
x = 5 
'''

# Example in code :
x = 5
name = 'Tim'
print (x)    # ---> Here the print() statement is used to print the variable value of x which is 5 when you run the program.
print(name)  # ---> Here the print() statement is used to print the variable value of name which is the string 'Tim' when you run the program.

'''
*** Important things to know about variables : *** 

An important thing to know is that python is case sensitive when it comes to declaring variables. 
And another thing to also know is if the exact variable is given a different value the value that will be stored in
the variable will change. 

So for example a user typed ( x = 5 ) and then printed x and then the user assigned a different value 
for the variable x as ( x = 10 ) and printed x again the value displayed this time will be 10 and not 5 as the value 
that is stored for the variable x was overwritten by the user when they assigned a new value of 10 
'''
# Example in code :
x = 5
print (x)
x = 10
print (x)
x = 'Osama'
print (x)
# Another way to show this would be like that :
x = 5
x = 10
x = 'Osama'
print (x)   # ---> When x is printed it will only display (Osama) as it was the last the previous values where overwritten.

'''
Some restrictions on variables : 

The variables that can be defined and understood by python should follow a certain set of rules: 
     {What can be included in Variable names} :
     [1] underscores like --> (person_name)
     [2] lower and upper case letters --> (name) , (Name) , (NAME)
     [3] end with a number or contains a number --> (na1me) , (name1) , (name_1)
     
     {What cannot be included in Variable names} :
     [1] spaces like --> (person name) 
     [2] dashes like --> (person-name)
     [3] starting with a number --> (1name)
     [4] special characters / symbols --> (name*) , (*name)
'''

''' 
Question (2) : 

Are they the same variable and what will be displayed ? 
{1} name = 40   ---> print(name) 
{2} NAME = 30   ---> print(NAME)
{3} Name = 10   ---> print(Name)
------------------------------------------------------
ANS: 
NO, they are not the same variables as (name) is all lower case , (NAME) is all upper case ,
and (Name) has the first letter as upper case and the rest are lower case. 

{1} print(name) ---> gives an output of (40) 
{2} print(NAME) ---> gives an output of (30) 
{3} print(Name) ---> gives an output of (10) 
'''
# Visualization of Question (2) using code :
name = 40
NAME = 30
Name = 10
print(name)
print(NAME)
print(Name)
