# coding=windows-1251
# 5 ���� 3 ������
print("����������� ����� ����������")
minimum = int(input())
print("�������� �����")
ivan = int(input())
print("�������� ������")
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