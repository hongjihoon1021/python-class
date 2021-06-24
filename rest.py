#리스트
season=['봄','여름','가을','겨울']
number=[1,5,2,4,3]
#변수 season 출력
print(season)
#문자열 season 출력
print('season')
#리스트 인댁싱
print(season[1])
print(number[0]+number[3])
print(number[-2])
#리스트슬라이싱
print(season[0:3])
#리스트 반복
print(number*2)
#변수개수새기
print(len(number))
#수정하기
number[4]=6
print(number)
#삭재
del number[4]
print(number)
del number[2:]
print(number)
num=[1,2,3,4,5,6,7,8,9]
del num[4:8]
print(num)
