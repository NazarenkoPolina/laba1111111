def proc1():

pas = input("Ведите пароль")

if len(pas) < 6:
    print("Слишком короткий пароль")
elif pas [0:7] =="qwerty":
    print ('Ненадежный пароль')

else:
    print("OK.")

def proc2():
    n = int(input('ВВедите номер вашего места в плацкартном вагоне: '))
    print()
if range (37,54) :    print('ваше место - боковое.')
elif n  % 2:    print('ваше место и купе внизу.')
else:
    print('ваше место в купе наверху.')

"""def proc3():
    year = int(input()) if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
print('ДАТ весокосный')
    else:
print('НЕТЪ не высокосный')"""


def proc4():
vvod1 = input("")
vvod2 = input("")
if (vvod1 == "красный" and vvod2 == "синий") or (vvod2 == "красный" and vvod1 == "синий"):
    print("фиолетовый")
if (vvod1 == "красный" and vvod2 == "желтый") or (vvod2 == "красный" and vvod1 == "желтый"):
    print("ораньжевый")
if (vvod1 == "синий" and vvod2 == "желтый") or (vvod2 == "синий" and vvod1 == "желтый"):
    print("зеленый")
if vvod1 or vvod2 != "красный" or "синий" or "желтый":    print("НЕ правильный цвет")
