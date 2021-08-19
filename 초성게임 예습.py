#시작화면-초성게임 예습.py
print('===============================')
print('게임 홈페이지에오신것을 환영 들입니다.')
print('당신의이름을 입력해주시면 감사하겠습니다.')
print('게인정보는 프로그램이 끝나면 자동페기 됩니다.')
while True:
    name=input('이름:')
    howold=int(input('나이'))
    print('감사드립니다%s님'%(name))
    if howold<=20:
        print('아이들을 위한 게임이시작될것입니다....')
        print('첫번쩨문제 입니다')
        print('ㅁ ㅇ ㅋ ㄹ ㅍ ㅌ')
        answer1=input('대답:(모르면 힌트라고입력해주세요)')
        if answer1=='마인크래프트':
            print(' 정답입니다')
            print('두번쩨문제 입니다')
            print('ㅍㅇㅆ')
                while True:
                    answer2=input('대답:(모르면 힌트라고입력해주세요)')
                    if answer2=='파이썬':
                        print(' 정답입니다')
                        print('세번쩨문제 입니다')
                        print('ㅇㅁㅇㅅ')
                        while True:
                            answer2=input('대답:(모르면 힌트라고입력해주세요)')
                                 if answer2=='어몽어스':
                                    print(' 정답입니다')
                                    print('당신이 이겼습니다.')
                                    print('게임이끝났읍니다.')
                                    print('어른버전도만들어 돌아오겠습니다.')
                                    exit()

                                  elif answer2=='힌트':
                                        print('마피아게임입니다..')
                                  else:
                                        print('틀렸읍니다')

                
                    elif answer2=='힌트':
                        print('컴퓨터프로그램입니다.')
                    else:
                        print('틀렸읍니다')

          elif answer1=='힌트':
                print('마크 라고도불림니다(게임)')
            else:
                print('틀렸읍니다')



                    
