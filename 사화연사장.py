num1,num2=map(int,input().split())
#if num1>num2:
#    _max=num1
#else:
#    _max=num2


_max=num1 if num1>num2 else num2
print(_max)
