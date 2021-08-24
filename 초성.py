#첫화면
print('===안녕하세요. 초성게임니다===')
print('게임을 시작하시겠습니다?(예,아니요)')
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
print('힌트를원하신다면 힌트라고 입력하세요')
print('ㅁㅅㅌ')
while True:
    answer1=input('입력하세요:')
    if  answer1=='뭅스터':
        print('정답입니다')
        break
    elif answer1=='힌트':
        print('https://jnhro1.github.io/으로 들어가보세요')
        continue
    else:
        print('틀렸읍니다')
        continue
print('두번쩨 문제입니다.')
print('마술 도구 이름입니다.')
print('ㅅㅇㅋㅋㄴㅅㅅ')
while True:
    answer2=input('입력하세요:')
    if answer2=='사이코키네시스':
        print('정답입니다.')
        break
    elif answer2=='힌트':
        print('https://www.youtube.com/results?search_query=%EB%8B%88%ED%82%A4+%EC%82%AC%EC%9D%B4%EC%BD%94%ED%82%A4%EB%84%A4%EC%8B%9C%EC%8A%A4로가세요')
        continue
    else:
        print('틀렸읍니다.')
        continue
print('세번쩨 문제입니다.')
print('뭅스터개발자로 아직까지 기간은 반이지났는데 20프로만 만든 사람이름')
print('조나현')
while True:
    answer3=input('입력하세요:')
    if answer3=='조나현':
        print('정답입니다.')
        break
    elif answer3=='힌트':
        print('https://jnhro1.github.io/으로 들어가보세요')
        continue
    else:
        print('틀렸읍니다.')
        continue
print('네번쩨 문제입니다.')
print('이사람은 다른사람의 엔트리계정을 등 용하는 나쁜사람입니다.')
print('ㄱㅁㅅ')
while True:
    answer4=input('입력하세요:')
    if answer4=='곽민성':
        print('정답입니다.')
        break
    elif answer3=='힌트':
        print('https://github.com/minsung0119')
        continue
    else:
        print('틀렸읍니다.')
        continue
print('네번쩨 문제입니다.')
print('it 기업.')
print('ㅇㅁㅈ')
while True:
    answer3=input('입력하세요:')
    if answer3=='아마존':
        print('정답입니다.')
        break
    elif answer3=='힌트':
        print('s3')
        continue
    else:
        print('틀렸읍니다.')
        continue

