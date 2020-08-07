x=123 # This is a global variable.

def display():
    x=678 #This is a local method
    print(x)
    print(globals()['x']) #Use the globals function and the global variable will be displayed
print (x)
z = display() # Addition: this is how a function is assigned to a variable.
