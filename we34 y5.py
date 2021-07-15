print('             안녕하세요.bmi측정기입니다.')
name=input('이름이무엇입니까?')
print('반갑습니다 %s 님'%name[1:3])
height=float(input('키를입력하세요(m)'))
if height>3:
    print('잘못입니다')
    exit(1)
weight=float(input('몸무계를입력하세요(kg)'))
def bmiFunc (height,weight):
    bmi=weight/(height*height)
    if bmi <= 18.5:
        result='=============저체중==============='
    elif bmi<=23:
        result='==========정상===================='
    elif bmi<=25:
        result='========체중의심========================'
    elif bmi<=30:
        result='==========비만================'
    else:
        result='========고도비만=========================================='
    return print(result)
bmiFunc(height,weight)
