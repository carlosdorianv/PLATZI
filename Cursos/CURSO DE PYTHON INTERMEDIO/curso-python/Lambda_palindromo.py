import string
from tokenize import String


# palindrome = lambda string: string == string[::-1]

# def palindrome (string):
#     try:
#         if len(string) == 0:
#             raise ValueError("No se puede ingresar una cadena vacia")
#         return string == string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False

# try:
#     print (palindrome("ana"))
# except TypeError:
#     print("Solo se pueden ingresar Strings")


def palindrome (string):
    assert len(string) > 0,"No se puede ingresar una cadena vacia"
    return string == string[::-1]

print (palindrome(""))


 