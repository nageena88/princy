# lst = []
# print(type(lst))
# print(len(lst))
# lst = [12, "Ram", 45.67, True, [34, 4], (1, 2), {1, 2, 3}, {"name": "Ram", "age": 34}]
# print(lst)

lst = [2, 4, 1, 5, 6, 7, 4, 3, 4]
# print(id(lst))
print(lst)
# insertion

# lst[0] = 100
# print(lst)
# print(id(lst))

# slice
# print(lst[:4])
# print(lst[2:5])
# print(lst[::2])
# print(lst[::-2])
# print(lst[::-1])

# deletion
# del lst[3]
# print(lst)

# del lst
# print(lst)

# traversal
# for item in lst:
#     print(item)

# print(len(lst))

# print(dir(lst))

methods = [
    # "append",
    # "clear",
    # "copy",
    # "count",
    # "extend",
    # "index",
    # "insert",
    # "pop",
    # "remove",
    # "reverse",
    # "sort",
]
# print(len(methods))
# print(methods.__len__())

# print(methods.__str__())

# lst.append(100)
# print(lst)

# lst.clear()
# print(lst)

# lst2 = lst.copy()
# print(lst2)
# print(lst)
# lst2[0] = 100
# print(lst2)
# print(lst)

# lst1 = lst
# print(lst1)
# print(lst)

# lst1[0] = 100
# print(lst1)
# print(lst)

# counter = lst.count(4)
# print(counter)

# lst1 = [1, 2, 3, 4]

# lst.extend(lst1)
# lst.append(lst1)
# print(lst)

# [2, 4, 1, 5, 6, 7, 4, 3, 4]

# idx = lst.index(4)
# print(idx)
# idx = lst.index(4, 3)
# print(idx)
# idx = lst.index(4, 2, 5)
# print(idx)
# idx = lst.index(10)
# print(idx)

# lst.insert(3, 100)
# print(lst)

# x = lst.pop()
# print(lst)
# print(x)

# x = lst.pop(3)
# print(lst)
# print(lst[3])
# print(x)

# lst.remove(4)
# print(lst)
# x = 4
# if x in lst:
#     lst.remove(x)
#     print(lst)

# lst.reverse()
# print(lst)

# lst.sort()
# print(lst)

# lst.reverse()
# print(lst)


# lst.sort(reverse=True)
# print(lst)

even = []
odd = []
for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)
