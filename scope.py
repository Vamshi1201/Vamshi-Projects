x = 99
y = 0

def example():
    global x
    x = 999
    global y
    y = 333
    print('in func x =',x)
    print('in func y =', y)

example()

print('outside x =', x)

print('outside y =', y)

print(globals()['x'])