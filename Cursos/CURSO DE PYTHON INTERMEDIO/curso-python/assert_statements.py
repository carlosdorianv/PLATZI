from unicodedata import numeric


def divisors(num):
    divisors =[i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    
    num = input('Ingresa un número: ')
    assert num.isnumeric() , "Debes ingresar un número"
    assert int(num) > 0 , "Debes ingresar un número positivo"
    print(divisors(int(num)))
    print('termino el programa')

if  __name__ == '__main__':
    run()

