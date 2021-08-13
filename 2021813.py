'''
2021813.py
'''
import turtle as t
print('이프로그램은 4가지프로그램이섞여 있읍니다순서대로실행되니 주의하십시오..')
print('1.printer progrem')
num1=input('문자를 입력하세요')
print('당신이입력한 문자는 %s 입니다.'%(num1))
print('2.+-*/progrem-1(다하기,빼기,나누기,곱하기)')
num2=int(input('정수를 입력하세요'))
num3=int(input('정수를 입력하세요'))
print('%d+%d=%d'%(num2,num3,num2+num3))
print('%d-%d=%d'%(num2,num3,num2-num3))
print('%d*%d=%d'%(num2,num3,num2*num3))
print('%d/%d=%d'%(num2,num3,num2/num3))
print('3.+-*/progrem-2(실수의 다하기,빼기,나누기,곱하기)')
num4=float(input('실수를입력해주세요'))
num5=float(input('실수를입력해주세요'))
print('%f+%f=%f'%(num4,num5,num4+num5))
print('%f-%f=%f'%(num4,num5,num4-num5))
print('%f*%f=%f'%(num4,num5,num4*num5))
print('%f/%f=%f'%(num4,num5,num4/num5))
print('4.터틀의예술품들')
t.color('red')
t.forward(-50)
t.write('서')
t.forward(50)
t.forward(100)
t.write('동')
t.left(145)
t.forward(100)
t.write('북')
t.left(-234)
t.forward(100)
t.write('남')








