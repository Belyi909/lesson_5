# coding=windows-1251
# 5 урок 3 задача
print("Минимальная сумма инвестиций")
minimum = int(input())
print("Средства Ивана")
ivan = int(input())
print("Средства Майкла")
mike = int(input())
if (ivan >= minimum) and (mike >= minimum):
    print(2)
elif (ivan >= minimum) and (mike <= minimum):
    print("Ivan")
elif (ivan <= minimum) and (mike >= minimum):
    print("Mike")
elif ((ivan + mike) >= minimum):
    print(1)
elif ((ivan + mike) < minimum):
    print(0)