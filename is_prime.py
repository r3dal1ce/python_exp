from lib2to3.pgen2.literals import evalString


i = int(input('Число -'))

def is_prime(i):
    if (i == 0):
        return False
    elif (i>1000):
        return "Число больше 1000!"
    elif (i % 2 == 0):
        return False
    else:
        return True

print(is_prime(i))  