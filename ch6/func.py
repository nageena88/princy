# no return no arguments
# no return with arguments
# with return no arguments
# with return with arguments

# add
# no return no arguments


def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Addition:", a + b)


# sub
# no return with arguments
def sub(a, b):
    print("Subtraction:", a - b)


# mul
# with return no arguments
def mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a * b


# div
# with return with arguments
def div(a, b):
    return a / b


# add()

# sub(10, 5)
# sub(24, 8)

# res = mul()
# print("Multiplication:", res)

# print("Division:", div(20, 4))
