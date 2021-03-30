# Lambda ( Which stands for an anonymous function )

def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 85

# --- In order to use the Lambda function you type it and give it any number of parameters
# --- just like the def function and then giving what it will return by using a colon.

func3 = lambda x: x + 5
print(func3(9))

# --- Using multiple parameters with lambda
func4 = lambda x, y: x + y
print(func4 (5, 5))

# --- Using multiple AND optional parameters with lambda like the def function basically.
func5 = lambda x, y=4: x + y
print(func5 (5))

print(func(2))

# --- The only difference between def and lambda is that when you are using the
# --- lambda function you can only return a single expression


# using the lambda with the map function and filter function
# --- the mapping function
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x + 5, a)) # --- Here we are mapping the whole lambda function on the a list
print(newList)

# --- the filter function
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList2 = list(filter(lambda x: x % 2 == 0, b)) # --- Here we are mapping the whole lambda function on the a list
print(newList2)