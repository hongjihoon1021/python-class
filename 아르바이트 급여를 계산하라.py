print('아르바이트 급여계산 프로그램')
print('※시급')
print('-주간 근무:9500원')
print('-야간 근무:주간 시급*1.5')
day=int(input('1(주간근무) 또는 2(야간 근무)을 입력해주세요;'))
time=int(input('근무 시간을 입력해 주세요'))

if day==1:
    work='주간'
    money=9500
else:
    work='야간'
    money=9500*1.5
print('%d시간 동안 일한 %s 급여는 %d원 입니다.'%(time,work,money*time))   
