# file = open("example.txt", "w")
# content = "This is an example content."
# file.write(content)
# print(file.closed)
# file.close()

# print(file.closed)

# with open("example.txt", "w") as file:
#     content = "This is an example content."
#     file.write(content)
#     print(file.closed)
# print(file.closed)

# with open("example.txt", "w") as file:
#     contents = [
#         "This is an example content.\n",
#         "This is the second line.\n",
#         "This is the third line.\n",
#     ]
#     print(file.tell())
#     file.writelines(contents)
#     print(file.tell())

# with open("example.txt", "r") as file:
#     print(file.tell())
#     content = file.read(10)
#     print(content)
#     print(file.tell())
#     content = file.read(10)
#     print(content)
#     print(file.tell())
#     content = file.read()
#     print(content)
#     print(file.tell())
#     file.seek(30)
#     print(file.tell())
#     content = file.read()
#     print(content)
#     print(file.tell())
# --------------------------
#     lines = file.readlines()
#     # print(lines)
#     for line in lines:
#         print(line, end="")
# --------------------------
#     for line in file:
#         print(line, end="")
# --------------------------
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()

# with open("example.txt", "a") as file:
#     file.write("This line is appended.\n")


# with open("example.txt", "wb") as file:
#     bytes_content = b"This is a bytes content.\n"
#     file.write(bytes_content)

# print("Bytes content written to the file.")
with open("example.txt", "rb") as file:
    bytes_content = file.read()

    print(bytes_content.decode("utf-8"))
