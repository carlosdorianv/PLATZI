def is_prime(int: int) -> bool:
    if int % 2 == 0 :
        return False
    return True    

def run():
    print(is_prime(3))

if __name__ == '__main__':
    run()
