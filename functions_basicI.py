#Predict the outcome of each function

#1
def a():
    return 5
print(a())
#5

#2
def a():
    return 5
print(a()+a())
#10

#3
def a():
    return 5
    return 10
print(a())
#5
#once it returns a value it will not run any other code in the function

#4
def a():
    return 5
    print(10)
print(a())
#5
#will not print 10 since it is after the return

#5
def a():
    print(5)
x = a()
print(x)
#5
#When the code is run, it is printing 5 and none and I am unsure why??

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#8
#When the code is run it is returning a "NoneType" error??

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#100
#10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#7
#14
#21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#500
#500
#300
#300

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#500
#500
#300
#300
#300
#Incorrect prediction, Unsure why a 3rd 300 won't print

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

