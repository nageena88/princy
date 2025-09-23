# type of operators in python
# x, y = 60, 13
# Arithmetic Operators
# +, -, *, /, //, %, **
# res = x + y
# print("Addition =", res)
# res = x - y
# print("Subtraction =", res)
# res = x * y
# print("Multiplication =", res)
# res = x / y
# print("Division =", res)
# res = x // y
# print("Floor Division =", res)
# res = x % y
# print("Modulus =", res)
# res = 2**4
# print("Exponent =", res)


# Assignment Operators
# =, +=, -=, *=, /=, //=, %=,
# a = 10
# print("a =", a)
# # x = x + 10
# x += 10
# print("x =", x)
# Comparison Operators
# ==, !=, >, <, >=, <=
# res = x == y
# print(res)
# res = x != y
# print(res)
# res = x > y
# print(res)
# res = x < y
# print(res)
# res = x >= y
# print(res)
# res = x <= y
# print(res)

# Logical Operators
# and, or, not
# res = True and False
# print(res)

# res = True or False
# print(res)

# res = not True
# print(res)

# Identity Operators
# is, is not

# x = "Hello"
# # y = "Hello"
# print(x[1:])
# y = "H" + x[1:]
# print(x is y)

# print(x == y)
# print(id(x))
# print(id(y))

# print(x)
# print(y)
# res = 0
# # print(res is None)
# print(res is not None)

# print(type(None))
# Membership Operators
# in, not in

# st = "This is a python programming language"
# print("Python" in st)
# lst = [1, 2, 2, 2, 1, 2, 3, 12, 23, 41, 231243, 121]
# print(12 in lst)
# print(100 not in lst)


# Bitwise Operators
# &, |, ^, ~, <<, >>

x, y = 60, 13
# res = x & y
# print(f"{x:06b}")
# print(f"{y:06b}")
# print("AND =", res)
# res = x | y
# print("OR =", res)
# res = x ^ y
# print("XOR =", res)
# res = ~x  # -(x+1)
# print("NOT =", res)
# print(~-41)

print(f"{x:08b}")

lshift = x << 3
print(f"{lshift:08b}")
print("Left Shift =", lshift)

rshift = x >> 3
print(f"{rshift:08b}")
print("Right Shift =", rshift)
