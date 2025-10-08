# t = ()
# print(type(t))  # <class 'tuple'>
# t = (1,)
# print(type(t))  # <class 'tuple'>
# print(t)  # (1,)

t = (1, 2, 3, 34, 45, 23, 12)
print(type(t))  # <class 'tuple'>
print(t)  # (1, 2, 3)


# print(t[0])
# print(t[-1])

# t[0] = 100
# # TypeError: 'tuple' object does not support item assignment

# del t[0]
# # TypeError: 'tuple' object doesn't support item deletion


# print(t[2:5])
# print(t[::2])

# slicing is possible in tuple as like list

# print(dir(t))

# 'count',
# counter = t.count(34)
# print(counter)
# # 'index',
# idx = t.index(34)
# print(idx)


# for x in t:
#     print(x)

# even = []
# for x in t:
#     if x % 2 == 0:
#         even.append(x)
# print(even)
