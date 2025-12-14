# x, y = 23, 0
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print("Error: Division by zero is not allowed.")
#     print(f"Exception details: {e}")
# print("This line will not be printed due to the exception above.")


class CustomException(Exception):
    def __init__(self, message=None):
        self.message = message


# with open("example.txt", "r") as file:
#     try:
#         x, y = 23, 0
#         print(x / y)
#         content = file.read()
#         print(content)
# except ZeroDivisionError as e:
#     print("An error occurred while reading the file.")
#     print(f"Exception details: {e}")
# except IOError as e:
#     print("An I/O error occurred.")
#     print(f"Exception details: {e}")
# except Exception as e:
#     print("An unexpected error occurred.")
#     print(f"Exception details: {e}")
# else:
#     print("File operations completed successfully.")
# finally:
#     print("File operations completed.")
#     print("This will be use to clean up resources.")
# n = 18
# for i in range(2, n):
#     if n % i == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")


# raise Exception


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            raise CustomException("Number is not prime")
    print("Number is prime")


try:
    prime(6)
except CustomException as e:
    print(e.message)
