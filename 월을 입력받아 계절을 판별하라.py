month=int(input('월을 숫자로 입력하세요'))

if month>=3 and month<=5:
    print('%d월은 봄입니다.'%month)
elif month>=6 and month<=8:
    print('%d월은 여름입니다.'%month)
elif month>=9 and month<=11:
    print('%d월은 가을입니다.'%month)
elif month==12 or month==1 or month==2:
    print('%d월은 겨울입니다.'%month)
else:
    print('잘못 입력하셨습니다')
