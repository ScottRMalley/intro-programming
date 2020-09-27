import sys

def add(x,y):
    return x+y

if(len(sys.argv) < 3):
    print('Please input two arguments')

print(add(int(sys.argv[1]), int(sys.argv[2])))
