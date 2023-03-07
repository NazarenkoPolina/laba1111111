vvod1 = input("")
vvod2 = input("")
if (vvod1 == "красный" and vvod2 == "синий") or (vvod2 == "красный" and vvod1 == "синий"):
    print("фиолетовый")
if (vvod1 == "красный" and vvod2 == "желтый") or (vvod2 == "красный" and vvod1 == "желтый"):
    print("ораньжевый")
if (vvod1 == "синий" and vvod2 == "желтый") or (vvod2 == "синий" and vvod1 == "желтый"):
    print("зеленый")
if vvod1 or vvod2 != "красный" or "синий" or "желтый":
    print("НЕ правильный цвет")
