print('Банк!')
a = float(input('Сколко денег положить? -'))
years = int(input('На сколько лет? - '))

def bank(a, years):
    for year in range(years):
       a *= 1.1
    return a

print(bank(a,years))