# st = "this is python programming language"
# print(st)
# print(type(st))
# st = 'this is "python" programming language'
# st = 'I don\'t know "python" programming language'
# print(type(st))
# print(st)
# -----------------------------------------------
st = "this is python programming language"
print(st)
# print(st[0])
# print(st[-7])

# st[0] = "T"
# del st[0]
# print(st)

# slicing
# print(st[0:5])
# print(st[5:10])
# print(st[:10])
# print(st[10:])

# print(st[::-1])
# print(st)
# print(dir(st))

methods = [
    # "capitalize",
    # "casefold",
    # "center",
    # "count",
    # "encode",
    # "endswith",
    "expandtabs",
    # "find",
    # "format",
    # "format_map",
    # "index",
    # "isalnum",
    # "isalpha",
    # "isascii",
    # "isdecimal",
    # "isdigit",
    # "isidentifier",
    # "islower",
    # "isnumeric",
    # "isprintable",
    # "isspace",
    # "istitle",
    # "isupper",
    # "join",
    # "ljust",
    # "lower",
    # "lstrip",
    "maketrans",
    # "partition",
    # "removeprefix",
    # "removesuffix",
    # "replace",
    # "rfind",
    # "rindex",
    # "rjust",
    # "rpartition",
    # "rsplit",
    # "rstrip",
    # "split",
    # "splitlines",
    # "startswith",
    # "strip",
    # "swapcase",
    # "title",
    "translate",
    # "upper",
    # "zfill",
]

# print(len(methods))
# print(len(st))

# res = st.capitalize()
# print(res)
# print(st)

# res = st.casefold()
# print(res)

# res = st.center(100)
# res = st.center(100, "-")
# print(res)
# res = st.center(50, "-")
# print(res)
# res = st.ljust(50, "-")
# print(res)
# res = st.rjust(50, "-")
# print(res)

# res = st.count("is")
# print(res)
# res = st.count("is", 3)
# print(res)
# res = st.count("is", 0, 5)
# print(res)

# res = st.count("Is")
# print(res)

# res = st.encode()
# print(res)
# print(type(res))

# res = st.endswith("language")
# print(res)
# res = st.startswith("This")
# print(res)

# "find",
# res = st.find("is", 4)
# print(res)
# "rfind",
# res = st.rfind("is")
# print(res)
# res = st.find("java")
# print(res)
# "index",
# res = st.index("is")
# res = st.index("is", 4)
# print(res)
# res = st.index("java")
# print(res)
# "rindex",
# res = st.rindex("is")
# print(res)


# "format",
# st1 = "My name is {} and my age is {}"
# print(st1)
# name = "Princy"
# age = 25
# res = st1.format(name, age)
# print(res)
# x, y = 10, 3
# print("{} is not divisible by {}".format(x, y))
# print(f"{x} is not divisible by {y}")
# "format_map",

# d = {"name": "Princy", "age": 25, "city": "Pune"}
# st1 = "My name is {name} and my age is {age}"
# res = st1.format_map(d)
# print(res)

# "isalnum",
# res = st.isalnum()
# print(res)
# "isalpha",
# res = st.isalpha()
# print(res)
# "isascii",
# "isdecimal",
# "isdigit",
# "isidentifier",
# "islower",
# res = st.islower()
# print(res)
# "isnumeric",
# "isprintable",
# "isspace",
# # "istitle",
# res = st.istitle()
# print(res)
# "isupper",
# res = st.isupper()
# print(res)


# res = st.upper()
# print(res)

# res = res.lower()
# print(res)

# res = st.title()
# print(res)

# res = res.swapcase()
# print(res)


# "join",

# s1 = "Ram"
# s2 = "Princy"

# res = s1.join(s2)
# print(res)

# st_split = st.split()
# print(st_split)
# # print(len(st_split))
# res = ",".join(st_split)
# print(res)

# res1 = res.split(",")
# print(res1)

# s = "fahrenheit = (c * 9 / 5) + 32"
# res = s.split("=")[-1]
# print(res)

# s = "    This is a python   programming   language    "
# # "lstrip"
# res = s.lstrip()
# print(res)
# # "rstrip"
# res = s.rstrip()
# print(res)
# # "strip"
# res = s.strip()
# print(res)

# s = """This is a python programming language.
# It is widely used language.
# It is easy to learn language.
# It is object oriented language.
# It is interpreted language."""

# # "splitlines",
# res = s.splitlines()
# print(res)

# res = st.zfill(50)
# print(res)

# "partition"
# res = st.partition("is")
# print(res)

# res = st.rpartition("is")
# print(res)

# s = "fahrenheit = (c * 9 / 5) + 32"
# res = s.partition("=")
# print(res)


# "removeprefix",
# res = st.removeprefix("this is py")
# print(res)
# # "removesuffix",
# res = st.removesuffix("mming language")
# print(res)
# "replace",

# res = st.replace(" is", " was")
# print(res)

# "maketrans"
# "translate",

# s1 = "aeiou "
# s2 = "AEIOU-"
# res = st.maketrans(s1, s2)
# print(res)
# res = st.translate(res)
# print(res)


for x in st.split():
    print(x)
