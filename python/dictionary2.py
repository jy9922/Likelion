information = {"����":"����", "���":"��ȭ����","�����ϴ� ����":"����"}
foods = ["�����", "����", "��������"]
print(information.get("���"))
information["Ư��"] = "�ǾƳ�"
information["��°�"] = "����"
del information["�����ϴ� ����"]
print(information)
print(len(information))
information.clear()
print(information)
print(foods[3])
print(foods[-1])
foods.append("���")
del foods[1]