# if
# if else
# ladder if
# nested if

# x, y = 30, 20
# if x > y:
#     print("x is Greater")
#     if x > 50:
#         print("x is also Greater than 50")
#     print(x)
# else:
#     print("y is Greater")
#     print(y)

# st = "This is a python programming language"
# if "python" in st:
#     st = st.replace("python", "Java")
# print(st)

# a, b = 1000, 200
# if a > b:
#     print("b is smaller")
# else:
#     print("a is smaller")


a, b, c = 3000, 2009, 3009

res = 0
# if a > b and a > c:
#     res = a
# elif b > c:
#     res = b
# else:
#     res = c
# print("Largest =", res)


if a > b:
    if a > c:
        res = a
    else:
        res = c
elif b > c:
    res = b  # res = b
else:
    res = c
print("Largest =", res)
