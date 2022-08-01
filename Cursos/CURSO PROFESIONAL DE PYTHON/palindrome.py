import re
from xmlrpc.client import boolean


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome(1000))   
    # Ana == anA
if __name__ == '__main__':
    run()

#mypy palindrome.py --check-untyped-defs
#sirve para encontrar los errores de type con mypy