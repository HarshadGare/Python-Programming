
def add1():
    add = 20+30
    print(add)
    return         # it indicate Exit From the Function


add1()


def addr():
    add = 200+30
    return add     # it indicate Exit From the Function


print(addr())


# ************ FUNCTION ARGUMENT TYPES **************
# 1. Required Argument
def add2(a, b):
    add = a + b
    print(add)


add2(10, 30)


# 2. Keyword Argument
def add3(name, age):
    print(name)
    print(age)


add3(age=19, name='harshad')


# 3. Default Argument
def add4(name, age=18):
    print(name)
    print(age)


add4(name='harshad')
add4(name='harshad', age=19)


# 4. Variable Length Argument
def info(n1, *n):
    print(n1)
    for x in n:
        print(x)


info(10)
info(10, 20)
info(50, 60, 40)
