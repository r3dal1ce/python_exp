day = int(input())
month = int(input())
year = int(input())

def date_cheat(day, month, year):
    import datetime # Импорт календаря
    try:
        datetime.date(year, month, day) # сравниваем введенные данные с календарем
    except ValueError: #Сообщение об ошибке в значении
        return False
    else:
        return True

print(date_cheat(day, month, year))