d = {}

def question():
    while True:
        q = input("질문을 입력해주세요 : ")
        if q == "q":
            break
        else:
            d[q] = ""
            
def answer(d):
    for i in d:
        a = input(i)
        d[i] = a
    print(d)

question()
answer(d)
    