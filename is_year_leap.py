print('Привет! Какой сейчас год?')
year = int(input('Сейчас - '))


def is_year_leap():
    if(year % 400 == 0):
        return True
    elif(year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

print(is_year_leap())
