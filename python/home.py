
import random

q_list = [
    {'질문' : '집밖에 나가는 것 자체가 스케줄?', '답변' : ''},
    {'질문' : '불금에는 북적대는 곳보단 집이지?', '답변' : ''},
    {'질문' : '휴대폰만 있어도 안 심심한가요?', '답변' : ''},
    {'질문' : '카톡, 문자 알림을 잘 확인하지 않나요?', '답변' : ''},
    {'질문' : '아무 생각이 없다. 왜냐하면 아무 생각이 없기 때문이다 라고 자주 느끼나요?', '답변' : ''},
    {'질문' : '당신은 배달앱 VIP인가요?', '답변' : ''},
    {'질문' : '친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 오예!라는 생각이 더 자주 드나요?', '답변' : ''},
]

sampleList = []
name = input('당신의 이름은? ')

def qna(name):
    global q_list, sampleList
    truecnt = 0
    result = 0
    print('====안녕하세요'+name+'님, 당신은 집순이일까요?====')
    print('====모든 질문의 대답을 네, 아니오로 답변해주세요====')
    cnt = int(input('받을 질문의 개수를 입력해주세요(최대 7개 가능): '))
    
    random.shuffle(q_list)
    
    for i in sampleList:
        print(sampleList[i]['질문'])
        answer = input('답변: ')
        q_list[i]['답변'] = answer
        
        if answer == '네':
            truecnt += 1
            
    result = truecnt / cnt * 100
    return result

def your_type(percent):
    if percent  >= 75:
        print('당신은 집순이 입니다.')
    elif percent >= 50:
        print('당신은 집에 있는 걸 조금 더 좋아합니다.')
    elif percent >= 25:
        print('당신은 밖에 있는 걸 조금 더 좋아합니다.')
    else:
        print('당신이 바깥순이 입니다.')
        
percent = qna(name)
your_type(percent)