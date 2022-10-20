

import sys
print('The command line arguments are')
for i in sys.argv:
    print(i)
print('\nThe PythonPath is',sys.path)

def add(x,y):
    return x+y
def mul(x,y):
    return x*y