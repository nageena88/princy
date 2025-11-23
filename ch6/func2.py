# def add(a, b, c):
#     return a + b + c


# def add(a, b):
#     return a + b


# def add(*args):
#     t = 0
#     for x in args:
#         t += x
#     return t


# print(add(1, 2, 3))
# print(add(1, 2))
# print(add(1, 2, 3, 4, 5))


# def student(name, std_class, **kwargs):
#     print(kwargs)
#     print(f"Name: {name}")
#     print(f"Class: {std_class}")
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")


# student(name="Alice", std_class="10th", age=20, major="Computer Science")


def func(a, b=2, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


func(1, 3, 4, 5, x=10, y=20)
