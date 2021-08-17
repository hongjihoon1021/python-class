#첫화면
print('안녕하세요. 초성게임니다')
print ('게임을 시작하시겠습니다?(예,아니요)')
while True:
    startAnswer=input()
    if startAnswer=='예':
        print('게임시작')
        break
    elif startAnswer=='아니요':
        print('게임종료')
        #프로그램 강제종료
        exit()
    else:
        print('잘못된대답')
print('첫번제 문제입니다')
print('홈페이지이름 입니다')
print('ㅁㅅㅌ')
while True:
    answer1=input()
    if  answer1=='뭅스터':
        print('정답입니다')
        break
    else:
        print('틀렸읍니다')
