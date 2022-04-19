print('Определяем сезон!')
a = int(input('Какой сейчас месяц по счету? - '))

def seasons(a):
    if a in (12,1,2):
        return "Зима!"
    elif a in (3,4,5):
        return "Весна!"
    # elif(a in 6,7,8):
    #     print('Лето!')
    # elif(a in 9,10,11):
    #     print('Осень!')
    else:
        return "Такого месяца не существует!"

print(seasons(a))