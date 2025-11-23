from pathlib import Path

# file_path = Path(__file__)
# print(file_path)
# path = Path(".")
# print(path.absolute())
path = Path(r"E:\princy\path_data")
# print(path)
print(path.exists())

# parent_path = path.parent.parent
# print(parent_path)

# if path.exists():
#     file_path = path.joinpath("princy.txt")
#     print(file_path)
# if file_path.exists():
#     print("file exists")
# else:
#     file_path.touch()

# file_path.write_text("Hello, this is a sample text file.")
# content = file_path.read_text()
# print(content)

parent_path = path.parent
print(parent_path)

# files = parent_path.glob("*.*")
# print(list(files))
# for file in files:
#     # if file.is_file():
#     #     print(file.name)
#     #     print(file.suffix)
#     #     print(file.stem)
#     #     print(file.stat().st_size)

#     # if file.is_dir():
#     #     print(file.name)
#     print(file.as_posix())


files = parent_path.rglob("path_data")
# print(list(files))
for f in files:
    f_path = f.joinpath("data")
    if f_path.exists():
        print(f_path)
    else:
        f_path.mkdir()
