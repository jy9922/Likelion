lunch = ["�����", "����", "��������", "¥���"]

while True:
    print(lunch)
    item = input("������ �߰����ּ��� : ")
    if item == "q":
        break
    else:
        lunch.append(item)
        
print(lunch)
set_lunch = set(lunch)