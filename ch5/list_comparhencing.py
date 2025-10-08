lst = [1, 4, 2, 5, 3, 6, 8, 4, 8, 9, 7]
print("lst:", lst)
# 1. Get all even numbers from the list
# even = []
# for x in lst:
#     if x % 2 == 0:
#         even.append(x)
# print(even)

# even = [x for x in lst if x % 2 == 0]

# print("even : ", even)

odd = (x for x in lst if x % 2 != 0)
# print("odd : ", odd)

# print(odd.__next__())
# print(odd.__next__())
# print(odd.__next__())
# print(list(odd))  # convert to list

# print("odd : ", next(odd))
# print(list(odd))  # convert to list

for d in odd:
    print(d)
