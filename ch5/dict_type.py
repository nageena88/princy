# d = {}
# print(d)
# print(type(d))
# d1 = dict()
# print(d1)
# print(type(d1))


d = {"name": "princy", "age": 22, "city": "bangalore"}
print(d)

# print(d["name"])
# print(d["age"])
# print(d["city"])
# print(d)

# d["name"] = "princy raj"  # update key is existing key
# print(d)

# d["email"] = "princy.raj@example.com"  # add new key
# print(d)

# d["Name"] = "Ram Chauhan"
# print(d)

# del d["age"]
# print(d)

# print(dir(d))
methods = [
    # "clear",
    # "copy",
    # "fromkeys",
    # "get",
    # "items",
    # "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    # "values",
]

lst = ["name", "age", "city"]

# d1 = dict.fromkeys(lst)
# print(d1)

# d1 = dict.fromkeys(lst, "UN")
# print(d1)


# dct = {}
# for x in lst:
#     dct[x] = input(f"Enter {x}: ")
# print(dct)

# name = d.get("name", "Ram Chauhan")
# print(name)
# print(d)

# name = d.get("Name", "Ram Chauhan")
# print(name)
# print(d)

# name = d.get("Name")
# print(name)
# print(d)

# d["marks"] = [12, 2, 34, 45]

# if d.get("marks") is not None:
#     avg = sum(d["marks"]) / len(d["marks"])
#     print(f"Average marks: {avg}")


# items = d.items()
# print(list(items))

# keys = d.keys()
# print(list(keys))

# values = d.values()
# print(values)

# val = d.pop("name")
# print(val)
# print(d)

# if d.get("name") is not None:
#     val = d.pop("name")
#     print(val)
# print(d)

# info = d.popitem()
# print(info)
# print(d)

# info = d.setdefault("name", "Ram Chauhan")
# print(info)
# print(d)

# # d1 = {"name": "Princy Raj", "salary": 10000}
# d.update(d1)

# print(d)


# for x in d:
#     print(x, end="=>")
#     print(d[x])


# for key in d.keys():
#     print(key, end="=>")
#     print(d[key])


# for value in d.values():
#     print(value)

# for key, val in d.items():  # key, value = (key, value) unpacking
#     print(key, "=>", val)
