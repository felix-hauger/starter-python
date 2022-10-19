
# '*' before the 'params' make it possible to use any number of arguments
def myFunction(*params):
    print(*params)

myFunction(1, 7.5, 'toto', True)