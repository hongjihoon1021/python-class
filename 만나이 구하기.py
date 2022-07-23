now_year=int(input('현재년은?'))
now_month=int(input('현재월은?'))
now_day=int(input('현재일은?'))
birth_year=int(input('출생년은?'))
birth_month=int(input('출생월은?'))
birth_day=int(input('출생일은?'))
if now_month>birth_month:
    age=now_year-birth_year
elif now_month==birth_month:
    if now_day>birth_day:
        age=now_year-birth_year
    else:
        age=now_year-birth_year-1
else:
    age=now_year-birth_year-1
print('만 나이:%d'%age) 
