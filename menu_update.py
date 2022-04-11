import datetime

dessert = {"초코 케이크" : 7000, "치즈 케이크" : 6000}
beverage = {"청포도 에이드" : 5500 , "아메리카노" : 4500}
total_cost = 0
dshopping_list = []
bshopping_list = []
final_menu = []

print(">>>디저트 카페에 오신 것을 환영합니다<<<")
print()
print(">>>주문을 중단하고 싶으시다면 /'q'/를 눌러주세요! 아래는 메뉴판입니다<<<")
print()

while True:
    print("디저트류 >> " + str(dessert))
    print("음료류 >> " + str(beverage))
    print()
    print()
    ditem = input("장바구니에 담고싶은 디저트 1개를 추가해주세요 : ")
    if ditem == "q":
        break
    else:
        print(ditem + "메뉴가 장바구니에 담겼습니다.")
        dshopping_list.append(ditem)
        total_cost += dessert[ditem]
    
    print()
        
    bitem = input("장바구니에 담고싶은 음료 1개를 추가해주세요 : ")
    if bitem == "q":
        break
    else:
        print(bitem + "메뉴가 장바구니에 담겼습니다.")
        bshopping_list.append(bitem)
        total_cost += beverage[bitem]
    print("=================================================")

print()
print(">>>장바구니에 담긴 디저트를 알려드립니다<<<")   
print(dshopping_list)
print()
print()
print(">>>장바구니에 담긴 음료를 알려드립니다<<<")   
print(bshopping_list)
print()

set_dessert = set(dshopping_list)
set_beverage = set(bshopping_list)

while True:
    ditem = input("장바구니에 삭제하고 싶은 메뉴 1개를 선택해주세요 : ")
    print()
    if ditem == "q":
        break
    elif ditem in dshopping_list:
        set_dessert = set_dessert - set([ditem])
        print("현재 장바구니 현황입니다.")
        print(str(set_dessert), str(set_beverage))
        total_cost -= dessert[ditem]
    else:
        set_beverage = set_beverage - set([ditem])
        print("현재 장바구니 현황입니다.")
        print(str(set_dessert), str(set_beverage))
        total_cost -= beverage[ditem]

print(">>>최종 장바구니에 담긴 내역입니다<<<")
print("디저트 : "+ str(set_dessert) + " 음료 : " + str(set_beverage))
print()
print("==============영수증 출력==============")
now = datetime.datetime.now()
print("주문 시각 : " + str(now))
print("주문 내역 : " + str(set_dessert | set_beverage))
print()
print()
print("주문하신 메뉴와 총 금액은" + str(total_cost) + "원 입니다.")
print(">>>감사합니다<<<")

