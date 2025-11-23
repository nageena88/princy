# def student(name, age, address):
#     print("Name:", name)
#     print("Age:", age)
#     print("Address:", address)


# student("Alice", 20, "123 Main St")

# # student(20, "Alice", "123 Main St")

# # student(address="123 Main St", name="Alice", age=20)

# student("Ram", address="456 Park Ave", age=22)


# def student(name, age, address, country="USA"):
#     print("Name:", name)
#     print("Age:", age)
#     print("Address:", address)
#     print("Country:", country)


# student("Alice", 20, "123 Main St")
# student("Bob", 25, "456 Park Ave", "Canada")
# student("Charlie", 30, "789 Oak St")


# lst = [1, 2, 3, 4, 5]


# def add_to_list(element, lst=[]):
#     lst.append(element)
#     return lst


# print(lst)
# print(add_to_list(10, lst))  # Output: [10]
# print(add_to_list(20, lst))  # Output: [10, 20]
# print(add_to_list(30, lst))  # Output: [10, 20, 30]
# print(lst)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# # 5*4*3*2*1
# 5 * 4 * 3 * 2 * 1

# print(factorial(5))  # Output: 120


# anonymous_func = lambda x: x * x
# add = lambda a, b, c: a + b + c

# print(add(10, 20, 30))  # Output: 60


st = "unit=[kb]"
st1 = "unit=mb"
st2 = "unit='GB'"


def value_unit(st, get_unit=lambda x: x.split("=")[-1].strip("[]").upper()):
    return get_unit(st)


print(value_unit(st))  # Output: KB
print(value_unit(st1))  # Output: MB
print(value_unit(st2, lambda x: x.split("=")[-1].strip("'[]").upper()))  # Output: GB
