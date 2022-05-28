num1,num2,num3=map(int,input('세수를 입력하세요').split())
if num1>num2:
    if num1>num3:
        _max=num1
    else:
        _max=num3
elif num2>num3:
    _max=num2
else:
    _max=num3
print('입력받은 수중 가장 큰+수는 %d 입니다.'%_max)
