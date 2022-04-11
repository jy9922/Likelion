total_list = []

def question():
    while True:
        q = input("질문을 입력해주세요 : ")
        if q == "q":
            break
        else:
            total_list.append({"질문" : q, "답변" : ""})
            
def answer(d):
    for i in total_list:
        a = input(i["질문"])
        i["답변"] = a
    print(total_list)

question()
answer(total_list)
    