# File: 01_global.py

x = 5

def printX():
    global x
    print(x)

def changeX1():
    global x
    x = 20

def changeX2():
    x = 30

printX() # prints "5"
x = 10
printX() # prints "10"
changeX1()
printX() # prints "20"
changeX2()
printX() # prints "20" again
